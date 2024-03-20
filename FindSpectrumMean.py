
import ROOT
from ROOT import gStyle
gStyle.SetOptStat(0)


#need to edit:
#- name of the folfer to fit,
#- name of the file inside the FILTERED folder
#- array in line 19 with the list of the scintialltors tested 

# open .root file and navigate to the folder where thr energy histograms are stored. 
myFile = ROOT.TFile.Open("/Users/bertabeltran/SMUT/data/TestingScintillators/Scint_29_30_31_32/FILTERED/HcompassF_Scint_29_30_31_32_20240220_121440.root")
myFile.ls()
dir = myFile.GetDirectory("Energy");


#scintialltors that we have tested in this run from Chn0 to Chan 3
scint_list=[29,30,31,32]


hist=[]
canvas=[]
fit=[]
mean=[]
mean_err=[]
sigma=[]
sigma_err=[]

for i in range(0, 4):
    histoname='_F_EnergyCH{}@DT5751_1615;1'.format(i)
    hist.insert(i, dir.Get(histoname))

    # heavyly rebin the histogram to find the bin with the aproximate mean value (bin with more counts)
    his_rebin=hist[i].Clone()
    his_rebin.Rebin(105)
    approx_mean= his_rebin.GetXaxis().GetBinCenter(his_rebin.GetMaximumBin())

    # now we fit the original histogram with a gauss around aprox_mean 
    hist[i].Rebin(7)
    canvas.insert(i,  ROOT.TCanvas("c{}".format(i)," ",800,600))
    
     # fit and save channel 0 spectrum 
    hist[i].Fit("gaus", "", "",approx_mean-250,approx_mean+200) # for the old scintillators with  lower light yiled 
    # hist[i].Fit("gaus", "", "",approx_mean-350,approx_mean+350) # for the new LUXIUM scintillators with higher light yiled 
    fit.insert(i, hist[i].GetFunction("gaus"))
    mean.insert(i,fit[i].GetParameter(1))
    mean_err.insert(i, fit[i].GetParError(1))
    sigma.insert(i,fit[i].GetParameter(2))
    sigma_err.insert(i, fit[i].GetParError(2))

    hist[i].GetYaxis().SetTitleOffset(1.2) #1.2
    hist[i].Draw()
    canvas[i].Draw()
 
    scint='Scintillator #{}'.format(scint_list[i])
   
    leg = ROOT.TLegend(.7,.8,.9,.9)
    leg.AddEntry(hist[i],scint,"L")

    leg.Draw()

    means = 'Fit mean {:.1f} #pm {:.2f}'.format(mean[i],mean_err[i])
    sigmas = 'Fit sigma {:.1f} #pm {:.2f}'.format(sigma[i],sigma_err[i])
    print(means)
    print(sigmas)
    tex_fit=ROOT.TLatex(0.5,0.7,means); # for the old scintillators with  lower light yiled 
    #tex_fit=ROOT.TLatex(0.15,0.7,means);
    tex_fit.SetNDC();
    tex_fit.SetTextSize(0.04);
    tex_fit.Draw();

    tex_fits=ROOT.TLatex(0.5,0.65,sigmas);# for the old scintillators with  lower light yiled 
    #tex_fits=ROOT.TLatex(0.15,0.65,sigmas);
    tex_fits.SetNDC();
    tex_fits.SetTextSize(0.04);
    tex_fits.Draw();

    scint_png="/Users/bertabeltran/SMUT/data/Fitting_means/Scint_{}.png".format(scint_list[i])
    canvas[i].SaveAs(scint_png);







