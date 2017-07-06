
%read table
clear all;
data = xlsread('participant_data_10');
%preallocate vector
stimmdiff = zeros(1,839);
% creating loop that iterates through rows of first column and subtracts
% previous value
rows = 840;
for i = 2:rows
    stimmdiff(i-1) = data(i,1)- data(i-1,1);
end
stimmdiff
% error: stimulus_value - response
trial_error = zeros(1,839);
for i = 2:rows
 trial_error(i-1) = data(i,1) - data(i,2);
end
trial_error


response_diff = zeros (1,839);
for i = 2:rows
    response_diff(i-1) = data(i,3) - data(i,2)
end
response_diff

matpart4(:,1) = trial_error
matpart4(:,2) = stimmdiff
matpart4(:,3) = response_diff

matpart4(105,:) = []
matpart4(209,:) = []
matpart4(313,:) = []
matpart4(417,:) = []
matpart4(521,:) = []
matpart4(625,:) = []
matpart4(729,:) = []

stimmdiff(105) = []
stimmdiff(209) = []
stimmdiff(313) = []
stimmdiff(417) = []
stimmdiff(521) = []
stimmdiff(625) = []
stimmdiff(729) = []

trial_error(105) = []
trial_error(209) = []
trial_error(313) = []
trial_error(417) = []
trial_error(521) = []
trial_error(625) = []
trial_error(729) = []



indices1 = find(abs(matpart4(:,2)>3)); % delete rows where stimm_diff is >3
    matpart4(indices1,:) = [];  
    
indices2 = find(abs(matpart4(:,2)< -3)); % delete rows where stimm_diff is <-3
    matpart4(indices2,:) = [];  
    
indices3 = find(abs(matpart4(:,3)==0));%delete rows where participants made no real response (did not adjust color)
    matpart4(indices3,:) = [];  
    
    
    

%rows1 = length(matpart4)
%for n = 1:rows1
 %  if matpart4(n,2)< -5
  %     matpart4(n,:) = []
   %    
   %elseif matpart4(1,2) >5
    %   matpart4(n,:) = []
     % 
   %else
    %   n = n+1
        
  % end
  %rows1= length(matpart4)
%end


c = sqrt(2)/exp(-.5);
estimates = fit_s_curve_flag(matpart4(:,2), matpart4(:,1))
scatter(matpart4(:,2), matpart4(:,1));hold on
plot(min(matpart4(:,2)):max(matpart4(:,2)),estimates(1)*estimates(2)*c*(min(matpart4(:,2)):max(matpart4(:,2))).*exp(-((estimates(2)*(min(matpart4(:,2)):max(matpart4(:,2))).^2))),'r','LineWidth',2);

