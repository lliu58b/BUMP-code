%% This file is used to collect data and write them into .csv files
% The output portrays the relationship between error e and N

function data_e_N(lp, sp, rp)

% Modify the base error
error = 1/500000;

% Set the maximum number of computations for each e
t = 200000;

% Modify n
n = 24;

% Initializing the collection of data (a matrix)
collection = [];

% Loop error through a range of values
for ii = 1:50
    e = ii * error;
    c = simulation_1(n, t, lp, rp, sp, e);
    collection = [collection; c];
end

% Write the results into a .csv file
T = array2table(collection);
T.Properties.VariableNames(1:6) = {'n', 'N', 'lp', 'rp', 'sp', 'e'};
writetable(T, 'data_e_N_7.csv');

end