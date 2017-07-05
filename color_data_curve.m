%%
%read table
clear all;
data = xlsread('participant_data_5');
%preallocate vector
stimmdiff = zeros(1,959);
% creating loop that iterates through rows of first column and subtracts
% previous value
rows = 960;
for i = 2:rows
    stimmdiff(i-1) = data(i,1)- data(i-1,1);
end
stimmdiff
% error: stimulus_value - response
trial_error = zeros(1,5);
for i = 2:rows
 trial_error(i-1) = data(i,1) - data(i,2);
end
trial_error

matpart4(:,1) = trial_error
matpart4(:,2) = stimmdiff
matpart4(120,:) = []
matpart4(239,:) = []
matpart4(358,:) = []
matpart4(477,:) = []
matpart4(596,:) = []
matpart4(715,:) = []
matpart4(834,:) = []



stimmdiff(120) = []
stimmdiff(239) = []
stimmdiff(358) = []
stimmdiff(477) = []
stimmdiff(596) = []
stimmdiff(715) = []
stimmdiff(834) = []

trial_error(120) = []
trial_error(239) = []
trial_error(358) = []
trial_error(477) = []
trial_error(596) = []
trial_error(715) = []
trial_error(834) = []
c = sqrt(2)/exp(-.5);
estimates = fit_s_curve_flag(matpart4(:,2), matpart4(:,1))
scatter(stimmdiff, trial_error);hold on
plot(min(matpart4(:,2)):max(matpart4(:,2)),estimates(1)*estimates(2)*c*(min(matpart4(:,2)):max(matpart4(:,2))).*exp(-((estimates(2)*(min(matpart4(:,2)):max(matpart4(:,2))).^2))),'r','LineWidth',2);



