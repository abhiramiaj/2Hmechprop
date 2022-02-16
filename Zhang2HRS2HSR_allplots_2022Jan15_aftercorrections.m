clear all
clc
figure
%Young's moduli ratio 2H RS and 2H SR composites%%%%%
n=5; %number of platelets in each period in stairwise staggered composite
pr=0.5; %volume fraction of regular staggered composite (2HRS)
ps=0.5;  %volume fraction of Stairwise staggered composite
gbe=1/1000;%Gm/Ep;
z=0.5;
sigtotau=10;
subplot(1,2,1);
rr=0:1:100; %Aspect ratio of platelet in 2HRS composite
for rs=[10,20,40,80,160,320,450] %Aspect ratio of platelet in stairwise staggered composite, at the first level of hierarchy
    as=(ps.*rs.*rs.*gbe)./(3*(1-ps)); %alpha_s
    A=(((n.*((3*n)-4))./(3*((n-1).^2)))+(((n.*n)./(3*(n-1).*as))));
    ars=(pr.*rr.*rr.*gbe.*A)./(ps.*(1-pr).*3);%alpha_RS
    Erat=(A.*((4./3)+((1./((3*z.*(1-z).*ars)))))).^-1; %E_RS/E_p phi_R phi_S
    limitstiff=0.65;
    plot (rr,Erat,'linewidth', 1.5);
    hold on;
end
plot (rr,limitstiff*ones(size(rr)),'--','linewidth', 1.5);
xlabel ('\rho_{RS}', 'fontsize', 18,'fontweight','bold')
ylabel ('E_{RS}/Ep \phi_R \phi_S', 'fontsize', 18,'fontweight','bold')
legend ('\rho_S = 10', '\rho_S = 20', '\rho_S = 40', '\rho_S = 80','\rho_S = 160','\rho_S = 320','\rho_S = 450');
pbaspect([5 4 1])
set(gca,'fontsize',16)
% xlim([0 100])
% ylim([0 0.8])
set(gcf,'color','w')

subplot(1,2,2);
rs=0:1:100;%Aspect ratio of platelet in 2HSR composite
for rr=[10,20,40,80,160,320,450]%Aspect ratio RSM 1H
    ar=(pr.*rr.*rr.*gbe)./(3*(1-pr)); %alpha_R
    A=((4./3)+((1./((3*z.*(1-z).*ar)))));
    asr=(ps.*rs.*rs.*gbe*A)./(pr.*(1-ps).*3); %alpha_RS
    Erat=(A.*(((n.*((3*n)-4))./(3*((n-1).^2)))+(((n.*n)./(3*(n-1).*asr))))).^-1;%E_SR/E_p phi_R phi_S
    plot (rs,Erat,'linewidth', 1.5);
    hold on;
end
plot(rs,limitstiff*ones(size(rs)),'--','linewidth', 1.5);
xlabel ('\rho_{SR}', 'fontsize', 18,'fontweight','bold')
ylabel ('E_{SR}/Ep \phi_R \phi_S', 'fontsize', 18,'fontweight','bold')
legend ('\rho_R = 10', '\rho_R = 20', '\rho_R = 40', '\rho_R = 80','\rho_R = 160','\rho_R = 320','\rho_R = 450');
set(gca,'fontsize',16)
pbaspect([5 4 1])
% xlim([0 100])
% ylim([0 0.8])
%%%%%%%%%Strength ratio 2H RS and 2H SR Composites %%%%%%%%

figure
subplot(1,2,1);
rscrit=(n-1)*sigtotau;%critical aspect ratio in first level of hierarchy
 for rs=5:5:100
     if rs<=rscrit
         rrcrit=(ps*rs)./n; %critical aspect ratio in second level of hierarchy
     else
         rrcrit=(ps*sigtotau*(n-1))./n;
     end
     rr=0:1:120;
     y=zeros(size(rr));
     for i=1:numel(rr)
         if rr(i)<=rrcrit
             y(i) = rr(i)./(2*ps*sigtotau);%case 1 n 2
         elseif rr(i)>rrcrit && rs<=rscrit
             y(i)=(rs)./(2*n*sigtotau); %case 3
         else
            y(i)=(n-1)./(2*n);
         end
     end
     plot (rr,y,'linewidth',1.5)
     hold on;
 end
 xlim([0,120]) 
 ylim([0,0.42]) 
set(gca,'fontsize',16)
xlabel ('\rho_R_S','fontweight','bold', 'fontsize', 18)
ylabel ('\sigma^R^S_{critical}/ \phi_R \phi_S \sigma^P_{critical}','fontweight','bold', 'fontsize', 18)
legend({'\rho_S = 5', '\rho_S = 10', '\rho_S = 15', '\rho_S = 20','\rho_S = 25','\rho_S = 30','\rho_S = 35','\rho_S = 40'},'fontsize', 16)
pbaspect([5 4 1])


subplot(1,2,2);
rrcrit=sigtotau; %critical aspect ratio in first level of hierarchy
for rr=[5,40]
    if rr<=rrcrit
        rscrit=(n-1)*pr*rr*0.5; %critical aspect ratio in first level of hierarchy
    else
        rscrit=(n-1)*pr*sigtotau*0.5;
    end
    rs=0:1:120;
    y=zeros(size(rs));
    for i=1:numel(rs)
        if rs(i)<=rscrit
            y(i) = rs(i)./(pr*n*sigtotau);%case 1 n 2
        elseif rs(i)>rscrit && rr<=rrcrit
            y(i)=(rr.*(n-1))./(2*n*sigtotau);%case 3
        else
            y(i)=(n-1)./(2*n);%case 4
        end
    end
    plot (rs,y,'linewidth',1.5)
    hold on;
end
xlim([0,120])
ylim([0,0.42]) 
set(gcf,'color','w')
%title ('\sigma^S^R_{critical}/ \phi_R \sigma^P_{critical} for Stairwise Staggered platelets within Regular Staggered Composites','fontsize',25)
set(gca,'fontsize',16)
xlabel ('\rho_S_R','fontweight','bold', 'fontsize', 18)
ylabel ('\sigma^S^R_{critical}/ \phi_R \phi_S \sigma^P_{critical}','fontweight','bold', 'fontsize', 18)
legend({'\rho_R = 5', '\rho_R= 10', '\rho_R = 15', '\rho_R = 20','\rho_R = 25','\rho_R = 30','\rho_R = 35','\rho_R = 40'},'fontsize', 16)
pbaspect([5 4 1])


figure
%%%%%%%%%Strain ratio 2H RS and 2H SR Composites%%%%%%%%%%%%%
%for all values of n (4 CASES)
subplot(1,2,1);
rscrit=(n-1)*sigtotau;
for rs=5:10:45
    rr=0:1:120;
    y=zeros(size(rr));
    Ers=zeros(size(rr));
    ar=zeros(size(rr));
    if rs<=rscrit
        rrcrit=(ps*rs)./n;
    else
        rrcrit=(ps*sigtotau*(n-1))./n;
    end
    for i=1:numel(rr)
        A=(((n.*((3*n)-4))./(3*((n-1).^2)))+(((n.*n)./(3*(n-1).*as))));
        ars(i)=(pr.*rr(i).*rr(i).*gbe.*A)./((1-pr).*ps.*3);%alpha_RS
        Ers(i)=(((4/3)+(3*z.*ars(i).*(1-z)).^-1).^-1)*((n.*(3*n-4)/(3*((n-1).^2)))+(n.*n./(3*as.*(n-1)))).^-1;
        if rr(i)<=rrcrit
            y(i) = rr(i)./(2*ps*sigtotau*Ers(i)); %case 1 n 2
        elseif rr(i)>rrcrit && rs<=rscrit
            y(i)=(rs)./(2*n*sigtotau*Ers(i)); %case 3
        else
            y(i)=(n-1)./(2*n*Ers(i));%case 4
        end
    end
    plot (rr,y,'linewidth',1.5)
    hold on;
end
xlim([0,120])
ylim([0,140]) 
set(gca,'fontsize',16)
xlabel ('\rho_R_S','fontweight','bold', 'fontsize', 18)
ylabel ('\epsilon^R^S_{critical}/  \epsilon^P_{critical}\phi_R \phi_S','fontweight','bold', 'fontsize', 18)
legend({'\rho_S = 5', '\rho_S = 15', '\rho_S = 25', '\rho_S = 35','\rho_S = 45'},'fontsize', 16)
pbaspect([5 4 1])

subplot(1,2,2);
rrcrit=sigtotau;
for rr=5:10:45
    rs=0:1:120;
    y=zeros(size(rs));
    Esr=zeros(size(rs));
    asr=zeros(size(rs));
    ar=(pr.*rr.*rr.*gbe)./(3*(1-pr));
    A=((4./3)+((1./((3*z.*(1-z).*ar)))));
    if rr<=rrcrit
        rscrit=(n-1)*pr*rr*0.5;
    else
        rscrit=(n-1)*pr*sigtotau*0.5;
    end
    for i=1:numel(rs)
        asr(i)=(ps.*rs(i).*rs(i).*gbe*A)./(pr.*(1-ps).*3);
        Esr(i)=(A.*(((n.*((3*n)-4))./(3*((n-1).^2)))+(((n.*n)./(3*(n-1).*asr(i)))))).^-1;
        if rs(i)<=rscrit
            y(i) = rs(i)./(pr*n*sigtotau*Esr(i));%case 1 n 2
        elseif rs(i)>rscrit && rr<=rrcrit
            y(i)=(rr.*(n-1))./(2*n*sigtotau*Esr(i));%case 3
        else
        y(i)=(n-1)./(2*n*Esr(i));%case 4
        end
    end
    plot (rs,y,'linewidth',1.5)
    hold on;
end
xlim([0,120]) 
ylim([0,140]) 
set(gca,'fontsize',16)
xlabel ('\rho_S_R','fontweight','bold', 'fontsize', 18)
ylabel ('\epsilon^S^R_{critical}/ \epsilon^P_{critical}\phi_R \phi_S ','fontweight','bold', 'fontsize', 18)
legend({'\rho_R = 5', '\rho_R= 15', '\rho_R = 25', '\rho_R = 35','\rho_R = 45'},'fontsize', 16)
pbaspect([5 4 1])
set(gcf,'color','w')

figure
%%%%%%%%%Toughness ratio 2H RS and 2H SR composites%%%%%%%%%%
subplot(1,2,1);
rscrit=(n-1)*sigtotau;
for rs=5:10:45
    rr=1:1:120;
    [y,Ers,ars]=deal(zeros(size(rr)));
    if rs<=rscrit
        rrcrit=(ps*rs)./n;
    else
        rrcrit=(ps*sigtotau*(n-1))./n;
    end
    as=(ps.*rs.*rs.*gbe)./(3*(1-ps));
    for i=1:numel(rr)
        A=(((n.*((3*n)-4))./(3*((n-1).^2)))+(((n.*n)./(3*(n-1).*as))));
        ars(i)=(pr.*rr(i).*rr(i).*gbe.*A)./((1-pr).*ps.*3);%alpha_RS
        Ers(i)=(((4/3)+(3*z.*ars(i).*(1-z)).^-1).^-1)*((n.*(3*n-4)/(3*((n-1).^2)))+(n.*n./(3*as.*(n-1)))).^-1;
        if rr(i)<=rrcrit
            y(i) = rr(i)*rr(i)./(2*2*ps*ps*sigtotau*sigtotau*Ers(i));%case 1 n 2
        elseif rr(i)>rrcrit && rs<=rscrit
            y(i)=(rs*rs)./(2*2*n*n*sigtotau*sigtotau*Ers(i));%case 3
        else
            y(i)=((n-1).^2)/(2*2*n*n*Ers(i));%case 4
        end
    end
    plot (rr,y,'linewidth',1.5)
    hold on;
end
%  xlim([0,35]) 
%  ylim([0,45]) 
set(gca,'fontsize',16)
xlabel ('\rho_R_S','fontweight','bold', 'fontsize', 18)
ylabel ('w^R^S_{critical}/  w^P_{critical}\phi_R \phi_S','fontweight','bold', 'fontsize', 18)
legend({'\rho_S = 5', '\rho_S = 15', '\rho_S = 25', '\rho_S = 35','\rho_S = 45'})
pbaspect([5 4 1])

subplot(1,2,2);
rrcrit=sigtotau;
for rr=5:10:45
    rs=0:1:120;
    y=zeros(size(rs));
    Esr=zeros(size(rs));
    asr=zeros(size(rs));
    ar=(pr.*rr.*rr.*gbe)./(3*(1-pr));
    A=((4./3)+((1./((3*z.*(1-z).*ar)))));
    if rr<=rrcrit
        rscrit=(n-1)*pr*rr*0.5;
    else
        rscrit=(n-1)*pr*sigtotau*0.5;
    end
    for i=1:numel(rs)
        asr(i)=(ps.*rs(i).*rs(i).*gbe*A)./(pr.*(1-ps).*3);
        Esr(i)=(A.*(((n.*((3*n)-4))./(3*((n-1).^2)))+(((n.*n)./(3*(n-1).*asr(i)))))).^-1;
        if rs(i)<=rscrit
            y(i) = rs(i).*rs(i)./(pr*pr*n*n*sigtotau*sigtotau*Esr(i)); %case 1 n 2
        elseif rs(i)>rscrit && rr<=rrcrit
            y(i)=(rr.*rr.*((n-1).^2))./(2*2*n*n*sigtotau*sigtotau*Esr(i));%case 3
        else
            y(i)=((n-1).^2)./(2*2*n*n*Esr(i));%case 4
        end
    end
    plot (rs,y,'linewidth',1.5)
    hold on;
end
%  xlim([0,35]) 
%  ylim([0,20]) 
set(gca,'fontsize',16)
xlabel ('\rho_S_R','fontweight','bold', 'fontsize', 18)
ylabel ('w^S^R_{critical}/ w^P_{critical}\phi_R \phi_S ','fontweight','bold', 'fontsize', 18)
legend('\rho_R = 5', '\rho_R= 15', '\rho_R = 25', '\rho_R = 35','\rho_R = 45')
pbaspect([5 4 1])
set(gcf,'color','w')


