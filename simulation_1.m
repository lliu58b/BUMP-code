%% The simulation process takes in many inputs. n stands for the number of
% points on the circle, t is the number of steps, lp is the probability of
% going left, rp is the probability of going right, sp is the probability
% of staying in the same position. 

function simulation_1(n, t, lp, rp, sp)

% Instantiating the matrix we multiply to calculate the probability at each
% time t. 
M = diag(sp*ones(1,n)) + diag(rp*ones(1,n-1),1) + diag(lp*ones(1,n-1),-1);
M(1, end) = lp;
M(end, 1) = rp;

% Initializing probability: probability is 1 at the origin initially. 
v = zeros(1, n);
v(1, 1) = 1;
disp(M);
disp(v);

% Loops
for ii = 1:t
    v = v*M;
    disp(v);
end

end