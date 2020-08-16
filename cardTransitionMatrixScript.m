%This script finds the (n-1)! distinct classes of permutations
%(that is, it finds all configurations that aren't rotations of each other)
%INPUTS:
%n is number of cards
%p is probability of swapping any two cards

clc; clear all;
n = 5;
p = 0.1;
cards = linspace(1,n,n); %[1, 2, ..., n]
perms = perms(cards); %matrix of all permutations of cards
perm_classes = cell(factorial(n-1), n); %matrix of arrays storing all distinct card states 

for i = 1:factorial(n)
    new_perms = perms(i,:);
    for j = 1:n
        hasMatch = cellfun(@isequal, perm_classes, repmat({new_perms}, size(perm_classes)));
        [matchIndex, matchCol] = find(hasMatch, 1, 'first');
        if isempty(matchIndex)
            %try a new permutation ([1,2,3] -> [2,3,1])
            pop = new_perms(1);
            new_perms = new_perms(2:end);
            new_perms(end+1) = pop;
            if new_perms == perms(i,:)
                %this occurs when we've tried all permutations and come
                %back to our initial one.
                %permutation isn't part of an existing class
                for k = 1:factorial(n-1)
                    if isempty(perm_classes{k,1}) == 1
                        %find first empty column to add new permutation class
                        perm_classes{k,1} = new_perms;
                        break;
                    end
                end
            end
        else
            %permutation is part of an existing class. We'll fill these in
            %later.
            continue;
        end
    end
end

for i = 1:factorial(n-1)
    for j = 2:n
        pop = perm_classes{i,j-1}(1);
        perm_classes{i,j} = perm_classes{i, j-1}(2:end);
        perm_classes{i,j}(end+1) = pop;
    end
end

%OUTPUT is perm_classes. Check that variable. The first column is all the
%distinct classes, and the other columns are their permutations.

%Part II: Finding the transition matrix.
%FOR LARGER n (>= 6), USE transMatrix = sparse(factorial(n-1), factorial(n-1));
transMatrix = zeros(factorial(n-1), factorial(n-1));
for i = 1:factorial(n-1)
    for j = 1:n
        %Take the kth position and swap it. See which permutation class you
        %end up in.
        for k = 1:n
            swapped_perm = perm_classes{i,j};
            swap1 = perm_classes{i,j}(k);
            if k == n
                swap2 = perm_classes{i,j}(1);
                swapped_perm(k) = swap2;
                swapped_perm(1) = swap1;
            else
                swap2 = perm_classes{i,j}(k+1);
                swapped_perm(k) = swap2;
                swapped_perm(k+1) = swap1;
            end
            %find which permutation class it's in
            hasMatch = cellfun(@isequal, perm_classes, repmat({swapped_perm}, size(perm_classes)));
            [row, col] = find(hasMatch, 1, 'first');
            transMatrix(i,row) = transMatrix(i,row) + 1;
        end
    end
end

gcd = transMatrix(1,find(transMatrix~=0, 1, 'first'));
transMatrix = transMatrix ./ gcd;
%fill in the probabilities of state transitioning into other state
for i = 1:factorial(n-1)
    nnz = sum(transMatrix(i,:));
    transMatrix(i,:) = p.*transMatrix(i,:) ./ nnz;
end

%fill in the probabilities of state transitioning into itself
transMatrix(1:factorial(n-1)+1:end) = (1-p).*ones(1,factorial(n-1));
    
    

