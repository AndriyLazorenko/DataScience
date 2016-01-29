function [theta, J_history] = gradientDescent (X,y, theta, alpha, num_iters)
%Learns theta using gradient descent algorithm with learning rate alpha using number of iterations num_iters

m = length(y); % number of training examples
J_history = zeros (num_iters,1); %init J_history variable

for iter 1:num_iters
  predict = X*theta;
  errors = (predict-y);
  theta = theta - alpha / m * (X' * errors); %updating thetas simultaneously to thetas less learning times p.d. of cost fn
  J_history(iter) = computeCost (X,y, theta); %storing cost fn for visualization
end

end
