n = linspace(2, 101) %vector of 100 entries: 2, 3, 4, ..., 100, 101
error = linspace(0.4, 1, 10) %vector of 10 errors.
fArray = zeros(100,10);

for i = 1:100 %n range
    for j = 1:10 %error range
        fArray(i,j) = randomizingTime(n(i), error(j));
    end
end
[X, Y] = meshgrid(n, error);
mesh(X(1,:), Y(:,1), fArray')