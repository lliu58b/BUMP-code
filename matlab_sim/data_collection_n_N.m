%% This function is used to collect data and write them into .csv files
% The parameter n means from dividing the circle by 1 point to n points.
% Therefore, the output .csv file should have n lines

function data_collection_n_N(lp, rp, sp)

% Modify the amount of error we can bear 
error = 1/10000;

% Modify the maximum number of steps to take
t = 200000;

% Modify n 
n = 20;

% Initializing the collection of data (a matrix)
collection = [];

% Loop from 1 to n
for ii = 1:n
    c = simulation_1(ii, t, lp, rp, sp, error)
    collection = [collection; c];
end 

% Output to .csv file
T = array2table(collection);
T.Properties.VariableNames(1:6) = {'n', 'N', 'lp', 'rp', 'sp', 'e'};
writetable(T, 'data_asymmetrical.csv');

end