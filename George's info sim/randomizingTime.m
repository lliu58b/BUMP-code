function N = randomizingTime(n,epsilon)
%RANDOMIZINGTIME Given an n-point circle, finds the time taken until point is
%completely random below the tolerated epsilon.
L = 0.25; R = 0.25; S = 1 - L - R;
N = 0;
empirical_dist = [1 zeros(1,n-1)]; %Row vector
error = relative_entropy(empirical_dist, n);
hist = zeros(1,n);
while error > epsilon
    pos = 1; %Initial position of ball on circle
    for i = 1:max(50,n*n) %Run the simulation at least 50 times, or n*n times
        rand = randi(100)/100;
        if rand <= L %goes to the left
            pos = pos - 1;
        elseif rand > 1-R %goes to the right
            pos = pos + 1;
        end
    end
    final_pos = mod(pos, n) + 1; %to make the result from 1 to n instead of 0 to n-1
    disp(['final_pos on trial N=', num2str(N), ': ', num2str(final_pos)]);
    hist(final_pos) = hist(final_pos) + 1; %number of times it's landed on this position so far
    N = N + 1;
    empirical_dist = hist ./ (N .* ones(1,n)); %update empirical distribution
    error = relative_entropy(empirical_dist, n);
    disp(['error: ', num2str(error)]);
    disp(['empirical_dist: ', num2str(empirical_dist)]);
end
        
end

