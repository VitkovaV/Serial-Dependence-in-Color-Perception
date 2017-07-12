data = xlsread('Motivationtrials_1');
data(:,1) = data(:,1)+30 




%subtractnumber = 20 - addnumber


for i = 1:504
    addnumber(i) = rand()*30
end    


matrix(:,1) = addnumber
matrix(:,2) = 30-addnumber


data(:,3) = data(:,1) - matrix(:,2)
data(:,4) = data(:,1) + matrix(:,1)


xlswrite('data_response_bar_new.xls', data)

%for i = 1 : 504
 %   data(:,3) = 