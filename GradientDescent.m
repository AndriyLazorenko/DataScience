function [ thetas, iteration ] = GradientDescent( x, y )

%   GradientDescent uses incoming array as a data for learning and 
%returns Array of theta coefficients for linear regression solution
%to given problem using gradient descent method and returns number of
%iterations of gradient descent method used to achieve given thetas.

%Variables declarations

iteration = 0;
descentCoeff = 10^-2;
precisionCoeff = 10^-6;
dimension = length(x);
thetas = [1,1];

%Reusable fragment start

thetaZeroVector(1:dimension) = thetas(1);
hypothesis = thetaZeroVector + thetas(2)* x;
differences = hypothesis - y;
summDiffSqrd = sum(differences.^2);
costFunction = 1/2/dimension * summDiffSqrd;

%The gradient descent algorithm

while costFunction>precisionCoeff
    
   % working with thetas
   
   tempThetas(1) = thetas(1) - descentCoeff * 1/dimension * sum (differences);
   tempThetas(2) = thetas(2) - descentCoeff * 1/dimension * sum (differences.*x);
   thetas (1) = tempThetas(1);
   thetas (2) = tempThetas(2);
   
   % forward-chaining the thetas
   
   thetaZeroVector(1:dimension) = thetas(1);
   hypothesis = thetaZeroVector + thetas(2)* x;
   differences = hypothesis - y;
   summDiffSqrd = sum(differences.^2);
   costFunction = 1/2/dimension * summDiffSqrd;
   
   % iteration incrementation
   
   iteration = iteration+1;
   
   % catching the lagging algorithm
   
   if iteration == 10000
        break
   end
   
end
end
