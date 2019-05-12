function out=generate_kernel(num)
i=1:num;
%sum
a=ones(1,num)./num;
%stair
b=2*i./100;
%sin
c=sin(2*pi*i./num);
%sin 2x
d=sin(2*2*pi*i./num);
%sin 4x
e=sin(4*2*pi*i./num);

%for detail or supply
out=[a;b;c;d;e];
