%Code to find out combinations of aspect ratios for maximum stress and
%corresponding toughness
%there exist more than one combinations for maximum strength; the point
%with maximum toughness is selected
clear all
clc
figure
subplot(1,2,1);
Ep=7e12; %Young's modulus of platelet
Em=2.086e10; %Young's modulus of matrix
num=0.49; %Poisson's ratio of matrix
Gm=Em/(2*(1+num)); %Shear modulus of matrix
gbe=Gm/Ep; %Gm to Ep ratio
sigtotau=10; %Ratio of normal strength to shear strength of platelet and matrix
n1=2:1:10;  %swm 1H; no. of platelets in a period
ps1=0.5; %swm 1H; platelet volume fraction
pr2=0.5; %rsm 2H; platelet volume fraction
z2=0.5; %rsm 2H; overlap ratio


%%%%------------2HRS-----------%%%%
for m=1:numel(n1)
    rs1=1:1:120;
    [as,B,rr2crit2hrs,A,Z,Y]=deal(zeros(size(rs1)));
    for i=1:numel(rs1)
        rr2 = 1:1:120;
        [ars,Erat2hrs,E2hrs,sigrat2hrs, wrat2hrs]=deal(zeros(size(rr2)));
        for j=1:numel(rr2)
            as(i)=(ps1.*rs1(i).*rs1(i).*gbe)./(3*(1-ps1));
            B(i)=(((n1(m).*((3*n1(m))-4))./(3*((n1(m)-1).^2)))+(((n1(m).*n1(m))./(3*(n1(m)-1).*as(i)))));
            ars(j)=(pr2.*rr2(j).*rr2(j).*gbe.*B(i))./(ps1.*(1-pr2).*3);
            Erat2hrs(j)=(B(i).*((4./3)+((1./((3*z2.*(1-z2).*ars(j))))))).^-1;
            E2hrs(j)=Erat2hrs(j)*Ep*ps1*pr2;
            rs1crit2hrs=(n1(m)-1)*sigtotau;
            if rs1(i)<=rs1crit2hrs
                rr2crit2hrs(i)=(ps1*rs1(i))./n1(m);
            else
                rr2crit2hrs(i)=(ps1*sigtotau*(n1(m)-1))./n1(m);
            end
            
            if rr2(j)<=rr2crit2hrs(i)%case 1 n 2
                sigrat2hrs(j) = rr2(j)./(2*ps1*sigtotau);
                %wrat2hrs=rr2(j)*rr2(j)./(2*2*2*ps2*ps2*sigtotau*sigtotau*E2hrs)
                %%Alternate method            
            elseif rr2(j)>rr2crit2hrs(i) && rs1(i)<=rs1crit2hrs %case 3
                sigrat2hrs(j)=(rs1(i))./(2*n1(m)*sigtotau);
                %wrat2hrs=(rs1(i)*rs1(i))./(2*2*n1(m)*n1(m)*sigtotau*sigtotau*E2hrs)
            else %case 4
            sigrat2hrs(j)=(n1(m)-1)./(2*n1(m));
            %wrat2hrs=((n1(m)-1).^2)/(2*2*2*n1(m)*n1(m)*E2hrs)
            end
            wrat2hrs(j)=sigrat2hrs(j).^2/Erat2hrs(j);
            A(i,j)=wrat2hrs(j);
            Y(i,j)=sigrat2hrs(j);
            Z(i,j)=Erat2hrs(j);
        end
    end
    maxtough(m)=max(A(:));
    [rs1_maxtough, rr2_maxtough] = find(ismember(A, max(A(:))));
    maxstrength(m)=max(Y(:));
    [rs1_maxstrength, rr2_maxstrength] = find(ismember(Y, max(Y(:))));
    D=[rs1_maxstrength, rr2_maxstrength];
    q=size((rs1_maxstrength),1);
    r=size((rr2_maxstrength),1);
    for k=1:1:q
        for l=1:1:r
            E(m)=(A(rs1_maxstrength(k,1),rr2_maxstrength(l,1)));  %%%% edit this line to get the max toughness for the same strengths
        end
    end
    Q=rs1_maxstrength;
    R=rr2_maxstrength;
    rho1h_2hrs(m)=rs1_maxtough; %to extract the aspect ratios at maximum toughness
    rho2h_2hrs(m)=rr2_maxtough;
    strengthatmaxtough(m)=Y(rs1_maxtough,rr2_maxtough);
    stiffnessatmaxtough(m)=Z(rs1_maxtough,rr2_maxtough);
end
yyaxis left
plot (n1,maxtough,'o','MarkerSize',6,'Color','Blue','MarkerFaceColor','Blue')
%title('2HRS maximum toughness and corresponding strength vs n')
xlabel('n')
ylabel('w^{RS, max}_{critical}/\phi_R \phi_S w^{p}_{critical}')
yyaxis right
plot (n1,strengthatmaxtough,'s','MarkerSize',6,'Color','0.8500, 0.3250, 0.0980','MarkerFaceColor','0.8500, 0.3250, 0.0980')
ylabel('\sigma^{RS}_{critical}/\phi_R \phi_S\sigma^{p}_{critical}')
pbaspect([5 4 1])
legend ({'w^{RS, max}_{critical}/\phi w^{p}_{critical}','\sigma^{RS}_{critical}/\phi_R \phi_S \sigma^{p}_{critical}'},'fontsize',12)
set(gca,'fontsize',16)
set(gcf,'color','w')


subplot(1,2,2);
n2=2:1:10;  %swm 1H; number of platelets in a period
ps2=0.5; %swm 1H; platelet volume fraction
pr1=0.5; %rsm 2H; platelet volume fraction
z1=0.5; %rsm 2H; overlap ratio


%%%%%%%%%%%%2HSR**************
for m=1:numel(n2)
    rr1=1:1:120;
    [as,B,rr2crit2hrs,C,Z,Y,A]=deal(zeros(size(rr1)));
    for i=1:numel(rr1)
        rs2 = 1:1:120;
        [asr,Erat2hsr,E2hsr,sigrat2hsr, wrat2hsr]=deal(zeros(size(rs2)));
        for j=1:numel(rs2)
            ar(i)=(pr1.*rr1(i).*rr1(i).*gbe)./(3*(1-pr1));
            A(i)=((4./3)+((1./((3*z1.*(1-z1).*ar(i))))));
            asr(j)=(ps2.*rs2(j).*rs2(j).*gbe*A(i))./(pr1.*(1-ps2).*3);
            Erat2hsr(j)=(A(i).*(((n2(m).*((3*n2(m))-4))./(3*((n2(m)-1).^2)))+(((n2(m).*n2(m))./(3*(n2(m)-1).*asr(j)))))).^-1;
            E2hsr(j)=Erat2hsr(j)*Ep*ps2*pr1;
            rr1crit2hsr=sigtotau;
            if rr1(i)<=rr1crit2hsr
                rs2crit2hsr(i)=(n2(m)-1)*pr1*rr1(i)*0.5;
            else
                rs2crit2hsr(i)=(n2(m)-1)*pr1*sigtotau*0.5;
            end
            if rs2(j)<=rs2crit2hsr(i)
                sigrat2hsr(j) = rs2(j)./(pr1*n2(m)*sigtotau); %case 1 n 2
                
            elseif rs2(j)>rs2crit2hsr(i) && rr1(i)<=rr1crit2hsr %case 3
                sigrat2hsr(j)=(rr1(i).*(n2(m)-1))./(2*n2(m)*sigtotau);
            else
                sigrat2hsr(j)=(n2(m)-1)./(2*n2(m));%case 4
            end
            % epsrat2hsr(j)=sigrat2hsr(j)/E2hsr(j);
            wrat2hsr(j)=(sigrat2hsr(j)).^2/Erat2hsr(j);
            C(i,j)=wrat2hsr(j);
            Z(i,j)=Erat2hsr(j);
            Y(i,j)=sigrat2hsr(j);
        end
    end
    maxtough(m)=max(C(:));
    [rr1_maxtough, rs2_maxtough] = find(ismember(C, max(C(:))));
    maxstrength(m)=max(Y(:));
    [rr1_maxstrength, rs2_maxstrength] = find(ismember(Y, max(Y(:))));
    Q=rr1_maxstrength;
    R=rs2_maxstrength;
    strengthatmaxtough(m)=Y(rr1_maxtough,rs2_maxtough);
    stiffnessatmaxtough(m)=Z(rs1_maxtough,rr2_maxtough);
    rho1h_2hsr(m)=rr1_maxtough; %to extract the aspect ratios at maximum toughness
    rho2h_2hsr(m)=rs2_maxtough;
%     for k=1:1:size(Q)
%         fprintf('Toughness at (')
%         fprintf(num2str(Q(k)))
%         s=(Q(k));
%         t=(R(k));
%         fprintf(',')
%         fprintf(num2str(R(k)))
%         fprintf(')=')
%         fprintf(num2str(C(s,t)))
%         fprintf('\n')
%     end
   
 end
yyaxis left
plot (n2,maxtough,'o','MarkerSize',6,'Color','Blue','MarkerFaceColor','Blue')
% title('2HSR maxiimum toughness and corresponding strength vs n')
xlabel('n','fontsize',18)

ylabel('w^{SR, max}_{critical}/\phi_R \phi_S w^{p}_{critical}','fontsize',18)
yyaxis right
plot (n2,strengthatmaxtough,'s','MarkerSize',6,'Color','0.8500, 0.3250, 0.0980','MarkerFaceColor','0.8500, 0.3250, 0.0980')
ylabel('\sigma^{SR}_{critical}/\phi_R \phi_S\sigma^{p}_{critical}','fontsize',18)
pbaspect([5 4 1])

legend ({'w^{SR, max}_{critical}/\phi w^{p}_{critical}','\sigma^{SR}_{critical}/\phi_R \phi_S \sigma^{p}_{critical}'},'fontsize',12)
set(gca,'fontsize',16)
set(gcf,'color','w')