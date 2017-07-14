%read table
clear all;
data = xlsread('25_BP_FirstRealVersion_2017_Jul_14_1523.xlsx');


%data(505:510,:) = []
data(1:4,:) = []

data(63,:) = []
data(125,:) = []
data(187,:) = []
data(249,:) = []
data(301,:) = []
data(363,:) = []
data(425,:) = []


matrix(:,1) = data(:,2);
matrix(:,2) = data(:,1);
matrix(:,3) = data(:,3);
matrix(:,4) = data(:,24);
matrix


% min(matrix(:,4))
% max(matrix(:,4))

xvalue = matrix(:,4)+ 13.33
barvalue = (xvalue/26.66)*30

% min(barvalue)
% max(barvalue)

colorvalue = matrix(:,2) + barvalue


%preallocate vector
stimmdiff = zeros(1,496);
%creating loop that iterates through rows of first column and subtracts
%previous value
rows = 497;
for i = 2:rows
    stimmdiff(i-1) = matrix(i,1)- matrix(i-1,1);
end
stimmdiff
% error: stimulus_value - response
trial_error = zeros(1,496);
for i = 2:rows
 trial_error(i-1) = matrix(i,1) - colorvalue(i);
end

c = sqrt(2)/exp(-.5);
estimates = fit_s_curve_flag(stimmdiff, trial_error)
scatter(stimmdiff,trial_error);hold on
plot((min(stimmdiff):max(stimmdiff)),estimates(1)*estimates(2)*c*(min(stimmdiff):max(stimmdiff)).*exp(-((estimates(2)*(min(stimmdiff):max(stimmdiff)).^2))),'r','LineWidth',2);

