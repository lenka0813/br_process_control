close all
n=400;
m=30;
kenerl_w=generate_kernel(m);
x=2*rand(1,n);
x=x.^2;
out=con1d(x,kenerl_w,0);
% darw the kernel_w
figure(1)
plot(kenerl_w','.-');

%darw the 1d conv
figure(2)
plot(out');
hold on
plot(x(1:n-m),'k')

figure(3)
x=3*rand(1,n);
x=x.^2;
out1=con1d(x,kenerl_w,0);
plot(out1');
hold on
plot(x(1:n-m),'k')