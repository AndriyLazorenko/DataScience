function J = costFunction (X,y, theta)
%Cost function for linear regression
m = length(y); %number of training examples
predict = X*theta; % vectorized predicted values
errorsSqrd = (predict-y).^2; %squared errors
J = 1/(2*m)*sum(errorsSqrd); %cost function
end
