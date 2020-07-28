%% This function is used to check whether the probability is fully randomized. 
% Among the parameters, v is the vector of all the probabilities we have on
% each point, p is equal to the mean probability 1/n, e is the error we can
% bear. 

function randomized = check_equilibrium(v, p, e)

% Set default value as true
randomized = true;

% Set randomized to false if any of the entries deviates from 1/n beyond
% our tolerance
for jj = 1:length(v)
    if abs(v(jj) - p) > e
        randomized = false;
    end
end

end