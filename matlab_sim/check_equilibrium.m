%% This function is used to check whether the probability is fully randomized. 
% Among the parameters, u is the vector of all the probabilities we have on
% each point, p is equal to the mean probability 1/n, e is the error we can
% bear. 

function randomized = check_equilibrium(u, p, e)

% Set default value as true
randomized = true;

% Set randomized to false if any of the entries deviates from 1/n beyond
% our tolerance
for jj = 1:length(u)
    if abs(u(jj) - p) > e
        randomized = false;
    end
end

end