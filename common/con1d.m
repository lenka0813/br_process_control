function out=con1d(data,kernel,stride)
% do the conv op for the 1d signal
n=stride;
[n,m]=size(data);
[kn,km]=size(kernel);
out=zeros(kn,m-km);

if(n>m)
    m=n;
end

for i=1:m-km
    temp=data(:,i:i+km-1);
    temp=kernel*temp';
    out(:,i)=temp;
end
    
    
    
    
    
    
    
    
    
    
    
