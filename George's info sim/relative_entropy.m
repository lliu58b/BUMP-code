function D = relative_entropy(empirical, n)
%RELATIVE_ENTROPY finds the... relative entropy between this and the
%uniform distribution.

add = 0;
for i = 1:(n-1)
    if empirical(i) == 0
        continue;
    else
        add = add + empirical(i) .* log(empirical(i));
    end
end
D = log(n) + add;
end

