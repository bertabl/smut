
import ROOT
from ROOT import gStyle
gStyle.SetOptStat(0)

# open .root file and navigate to the folder where thr energy histograms are stored. 
myFile = ROOT.TFile.Open("/Users/bertabeltran/SMUT/data/TestingScintillators/Scint_10_14_15_16/FILTERED/HcompassF_Scint_10_14_15_16_20240129_113857.root")
myFile.ls()
dir = myFile.GetDirectory("Energy");


#scintialltors that we have tested in this run from Chn0 to Chan 3
scint_list=[10.1,14.1,15.1,16.1]
scint_fit_range=[700,1300,700,1300,700,1300,800,1400]

hist_0 = dir.Get("_F_EnergyCH0@DT5751_1615;1")
hist_0.Rebin(7)
c0 = ROOT.TCanvas("c0"," ",800,600)

hist_0.Fit("gaus", "", "",scint_fit_range[0],scint_fit_range[1])
gfit_0= hist_0.GetFunction("gaus")
m0=gfit_0.GetParameter(1)
m0_err= gfit_0.GetParError(1)
sig0=gfit_0.GetParameter(2)
sig0_err= gfit_0.GetParError(2)

hist_0.GetYaxis().SetTitleOffset(1.2) #1.2
hist_0.Draw()
c0.Draw()
 
scint0='Scintillator #{}'.format(scint_list[0])
# fit and save channel 0 spectrum 
leg0 = ROOT.TLegend(.7,.8,.9,.9)
leg0.AddEntry(hist_0,scint0,"L")

leg0.Draw()

mean_0 = 'Fit mean {:.1f} #pm {:.2f}'.format(m0,m0_err)
sigma_0 = 'Fit sigma {:.1f} #pm {:.2f}'.format(sig0,sig0_err)
print(mean_0)
print(sigma_0)

tex_fit0=ROOT.TLatex(0.5,0.7,mean_0);
tex_fit0.SetNDC();
tex_fit0.SetTextSize(0.04);
tex_fit0.Draw();

tex_fits0=ROOT.TLatex(0.5,0.65,sigma_0);
tex_fits0.SetNDC();
tex_fits0.SetTextSize(0.04);
tex_fits0.Draw();

scint0_png="/Users/bertabeltran/SMUT/data/Fitting_means/Scint_{}.png".format(scint_list[0])
c0.SaveAs(scint0_png);


# fit and save channel 1 spectrum 


hist_1 = dir.Get("_F_EnergyCH1@DT5751_1615;1")
hist_1.Rebin(7)
c1 = ROOT.TCanvas("c1"," ",800,600)

hist_1.Fit("gaus", "", "",1000,1500)
gfit_1= hist_1.GetFunction("gaus")
m1=gfit_1.GetParameter(1)
m1_err= gfit_1.GetParError(1)

hist_1.GetYaxis().SetTitleOffset(1.2) #1.2
hist_1.Draw()
c1.Draw()

scint1='Scintillator #{}'.format(scint_list[1])
leg1 = ROOT.TLegend(.7,.8,.9,.9)
leg1.AddEntry(hist_1,scint1,"L")

leg1.Draw()

mean_1 = 'Fit mean {:.1f} #pm {:.2f}'.format(m1,m1_err)
print(mean_1)

tex_fit1=ROOT.TLatex(0.5,0.7,mean_1);
tex_fit1.SetNDC();
tex_fit1.SetTextSize(0.04);
tex_fit1.Draw();

scint1_png="/Users/bertabeltran/SMUT/data/Fitting_means/Scint_{}.png".format(scint_list[1])
c1.SaveAs(scint1_png);


# fit and save channel 2 spectrum 


hist_2 = dir.Get("_F_EnergyCH2@DT5751_1615;1")
hist_2.Rebin(7)
c2 = ROOT.TCanvas("c2"," ",800,600)

hist_2.Fit("gaus", "", "",1000, 1500)
gfit_2= hist_2.GetFunction("gaus")
m2=gfit_2.GetParameter(1)
m2_err= gfit_2.GetParError(1)

hist_2.GetYaxis().SetTitleOffset(1.2) #1.2
hist_2.Draw()
c2.Draw()

scint2='Scintillator #{}'.format(scint_list[2])
leg2 = ROOT.TLegend(.7,.8,.9,.9)
leg2.AddEntry(hist_2,scint2,"L")

leg2.Draw()

mean_2 = 'Fit mean {:.1f} #pm {:.2f}'.format(m2,m2_err)
print(mean_2)

tex_fit2=ROOT.TLatex(0.5,0.7,mean_2);
tex_fit2.SetNDC();
tex_fit2.SetTextSize(0.04);
tex_fit2.Draw();

scint2_png="/Users/bertabeltran/SMUT/data/Fitting_means/Scint_{}.png".format(scint_list[2])
c2.SaveAs(scint2_png);


# fit and save channel 3 spectrum 


hist_3 = dir.Get("_F_EnergyCH3@DT5751_1615;1")
hist_3.Rebin(7)
c3 = ROOT.TCanvas("c3"," ",800,600)

hist_3.Fit("gaus", "", "",1000,1500)
gfit_3= hist_3.GetFunction("gaus")
m3=gfit_3.GetParameter(1)
m3_err= gfit_3.GetParError(1)

hist_3.GetYaxis().SetTitleOffset(1.2) #1.2
hist_3.Draw()
c3.Draw()

scint3='Scintillator #{}'.format(scint_list[3])
leg3 = ROOT.TLegend(.7,.8,.9,.9)
leg3.AddEntry(hist_3,scint3,"L")

leg3.Draw()

mean_3 = 'Fit mean {:.1f} #pm {:.2f}'.format(m3,m3_err)
print(mean_3)

tex_fit3=ROOT.TLatex(0.5,0.7,mean_3);
tex_fit3.SetNDC();
tex_fit3.SetTextSize(0.04);
tex_fit3.Draw();

scint3_png="/Users/bertabeltran/SMUT/data/Fitting_means/Scint_{}.png".format(scint_list[3])
c3.SaveAs(scint3_png);






