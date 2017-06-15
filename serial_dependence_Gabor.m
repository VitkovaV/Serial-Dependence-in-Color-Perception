-function [] = serial_dependence_Gabor(subj_ID, presentation_side)

    gaborsize = 600;
    %19 inch monitor, 1280x1024
    f = 0.009; % Grating cycles/pixel
    fr = f*2*pi; % frequency in radians/pixel
    contrast = .25;
    barwidth = 10;
    blur_filter = fspecial('gaussian', 35, 33);
    noise_size = 30;
    noise_contrast = 80;
    eccentricity = 235;
    clock_time = clock;
    rand('seed',clock_time(end));
    
    
    %% create and save the trial list
    trial_list = randi(180,[104 1])-90;
    
    if presentation_side == 'l'
        left_or_right = -1; %-1 for left, 1 for right
    elseif presentation_side == 'r'
        left_or_right = 1;
    else
        disp('invalid presentation side (use r or l)');
        return;
    end
    
    
    response_list = zeros(length(trial_list),1);    
    save_path = '/Users/jasonfischer/Desktop/serial_dependence_save';
    
    %handle duplicate filename
    if exist([save_path '/' subj_ID '.txt'],'file')
        overwrite = input('A file is already saved with this name. Overwrite? (y/n): ','s');
        if overwrite == 'y'
            %do nothing
        else %anything besides 'y', input new name
            subj_ID = input('Enter a new run identifier: ','s');
        end
        clear overwrite    
    end
    
    save_file = fopen([save_path '/' subj_ID '.txt'],'w');    
    fprintf(save_file,'orient:\tresp:\n\n');

    
    %% set up experiment
    AssertOpenGL;
    screens = Screen('Screens');
    screenNumber = max(screens);
    Screen('Preference', 'SuppressAllWarnings', 1);

    HideCursor();
    
    white = WhiteIndex(screenNumber);
    black = BlackIndex(screenNumber);
    gray = round((white+black)/2);

    [w screenRect]=Screen('OpenWindow',screenNumber, gray);
    Screen('BlendFunction', w, GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
    
    %create gaussian mask
    mask = ones(gaborsize+1, gaborsize+1, 2) * gray;
    [x,y] = meshgrid(-gaborsize/2:gaborsize/2,-gaborsize/2:gaborsize/2);
    mask(:, :, 2) = white * (1 - exp(-((x/75).^2)-((y/75).^2)));
    masktex = Screen('MakeTexture', w, mask);

    %create bar texgure
    bar = ones(gaborsize+1, gaborsize+1) * gray;
    bar(:,gaborsize/2+1 - barwidth:gaborsize/2+1 + barwidth) = white;
    bartex = Screen('MakeTexture', w, bar);
    
    %fix_rect & gabor_rect
    fix_rect = CenterRect([0 0 15 15], screenRect);
    gabor_rect = CenterRect([0 0 gaborsize+1 gaborsize+1], screenRect) + left_or_right*[eccentricity 0 eccentricity 0];
    gabor_srcRect=[0 0 gaborsize+1 gaborsize+1];

    spacebar = KbName('SPACE');
    esckey = KbName('ESCAPE');
    left_response = KbName('leftarrow');
    right_response = KbName('rightarrow');
    
    %display fixation point & instructions
    Screen('FillOval', w, white, fix_rect); %fixation dot
    Screen(w, 'TextSize',24);
    Screen(w,'DrawText','Press Space Bar to begin',50,50,255);
    Screen('Flip', w);
 
    %% start experiment
    
    priorityLevel = MaxPriority(w); 
    Priority(priorityLevel);
    
    % wait for spacebar
    [keyIsDown,seconds,keyCode] = KbCheck(-1);
    while ~keyCode(spacebar)
        [keyIsDown,seconds,keyCode] = KbCheck;
    end

    Screen('FillOval', w, white, fix_rect); %fixation dot
    Screen('Flip', w);
    prev_trial_end = GetSecs;
    
    for trial = 1:length(trial_list)
        
        %create oriented grating texture
        angle = trial_list(trial,1)*(pi/180); %convert from deg to rad
        a=cos(angle)*fr;
        b=sin(angle)*fr;
        grating = gray + (white - gray) * contrast * sin(a*x+b*y);
        gratingtex = Screen('MakeTexture', w, grating + imfilter(((resizem(rand(noise_size,noise_size),[gaborsize+1 gaborsize+1]) - .5)*noise_contrast/2),blur_filter,'replicate'));
        
        %create noise mask texgure
        noise = (resizem(rand(noise_size,noise_size),[gaborsize+1 gaborsize+1]) - .5)*noise_contrast + gray;
        noisetex = Screen('MakeTexture', w, imfilter(noise,blur_filter,'replicate'));
        
        %draw Gabor
        Screen('DrawTexture', w, gratingtex, gabor_srcRect, gabor_rect, 0);
        Screen('DrawTexture', w, masktex, gabor_srcRect, gabor_rect, 0);

        %fixation dot
        Screen('FillOval', w, white, fix_rect); %fixation dot

        
        while GetSecs < prev_trial_end+2;end %2s between trials
        
        
        Screen('Flip', w);
        
        WaitSecs(.5); %display stim for 500 ms

        % clear Gabor, display fixation & noise
        Screen('DrawTexture', w, noisetex, gabor_srcRect, gabor_rect, 0);
        Screen('DrawTexture', w, masktex, gabor_srcRect, gabor_rect, 0);
        
        Screen('FillOval', w, white, fix_rect); %fixation dot
        Screen('Flip', w);
        
        WaitSecs(1);
        
        Screen('FillOval', w, white, fix_rect); %fixation dot
        Screen('Flip', w);
        
        WaitSecs(.25);
        

%%      % adjust bar to respond

        bar_orient = floor(rand()*180); %randomize initial bar orientation
        
        %draw bar
        Screen('DrawTexture', w, bartex, gabor_srcRect, gabor_rect, bar_orient); %last argument is angle in degrees
        Screen('DrawTexture', w, masktex, gabor_srcRect, gabor_rect, bar_orient);
        
        %fixation dot
        Screen('FillOval', w, white, fix_rect); %fixation dot
        Screen('Flip', w);
        
        
        while 1
        [keyIsDown,seconds,keyCode] = KbCheck;
            if keyIsDown

                if keyCode(left_response)
                    bar_orient = bar_orient - 1;
                end

                if keyCode(right_response)
                    bar_orient = bar_orient + 1;
                end

                if keyCode(spacebar) %press space to submit response
                    break;
                end
                
                %draw bar in new orientation
                Screen('DrawTexture', w, bartex, gabor_srcRect, gabor_rect, bar_orient); %last argument is angle in degrees
                Screen('DrawTexture', w, masktex, gabor_srcRect, gabor_rect, bar_orient);

                %fixation dot
                Screen('FillOval', w, white, fix_rect); %fixation dot

                Screen('Flip', w); 

            end
        end
        
        %fixation dot alone
        Screen('FillOval', w, white, fix_rect); %fixation dot
        Screen('Flip', w);
        
        prev_trial_end = GetSecs;
        
        %record reponses, convert range to -90:89
        response_list(trial) = mod(bar_orient+90,180)-90;
        
        fprintf(save_file,'%i\t%i\n',trial_list(trial),response_list(trial)); %add trial to save file

        %Abort if escape is pressed
        [keyIsDown,seconds,keyCode] = KbCheck;
        if keyCode(esckey)
            break;
        end;

    end %end trials
    
    
    Priority(0);
    Screen('CloseAll');

    fclose(save_file);
    
    FlushEvents;
    
end %end main function



