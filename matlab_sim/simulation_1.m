%% The simulation process takes in many inputs. n stands for the number of
% points on the circle, t is the ceiling of the number of steps, lp is the 
% probability of going left, rp is the probability of going right, sp is 
% the probability of staying in the same position. e is the max error we 
% can tolerate when discussing whether all the probability of all points 
% are fully randomized. 

function w = simulation_1(n, t, lp, rp, sp, e)

% Instantiating the matrix we multiply to calculate the probability at each
% time t. 
if n == 2
    M = [sp (lp+rp); (lp+rp) sp];
else
    M = diag(sp*ones(1,n)) + diag(rp*ones(1,n-1),1) + diag(lp*ones(1,n-1),-1);
    M(1, end) = lp;
    M(end, 1) = rp;
end

% Initializing probability: probability is 1 at the origin initially. 
v = zeros(1, n);
v(1, 1) = 1;
disp(M);
disp(v);

% Continue steps when the number of steps does not exceed t and an
% equilibrium has not arrived
count = 0;
while count < t && ~check_equilibrium(v, 1/n, e)
    v = v*M;
    disp(count);
    disp(v);
    count = count + 1;
end

% Record the number of steps N as output, as well as other parameters. 
N = count;
w = [n, N, lp, rp, sp, e];
end