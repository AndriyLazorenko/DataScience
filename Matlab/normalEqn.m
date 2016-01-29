function [theta] = normalEqn (X,y)
%Analytical solution to linear regression using normal eqns
theta = pinv(X'*X)*X'*y;
end
