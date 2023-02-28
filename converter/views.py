from django.shortcuts import render
from currency_converter import CurrencyConverter
from datetime import date
from .forms import DataForm
from .models import Data
from django.http import HttpResponse

cc = CurrencyConverter()

def index(request):
	if request.method == "POST":
		form = DataForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			if not post.currency1 in currency_codes or not post.currency2 in currency_codes:
					return HttpResponse('<center>Wrong currency<br><br>You can use: <br>' + "<br> ".join(currency_codes))
			post.id = 1
			post.save()
	else:
		form = DataForm()
	first_currency = Data.objects.get(id=1).currency1
	second_currency = Data.objects.get(id=1).currency2
	amount = Data.objects.get(id=1).amount
	converted_amount = round(cc.convert(amount, first_currency, second_currency,), 3)
	context = {'form': form, 'first_currency': first_currency, 'second_currency': second_currency, 'amount': amount, 'converted_amount': converted_amount} 
	return render(request, 'converter/index.html', context)

currency_codes = ('AFN','ALL','DZD','USD','EUR','AOA','XCD','XCD','XCD','ARS','AMD','AWG','AUD','EUR','AZN','BSD','BHD','BDT','BBD','BYR','EUR','BZD','CFA','BCE','XOF','BMD','BTN','BOB','BAM','BWP','NOK','BRL','USD','BND','BGN','CFA','BCE','XOF','BIF','CVE','KHR','CFA','BEA','XAF','CAD','KYD','CFA','BEA','XAF','CFA','BEA','XAF','CLP','CNY','AUD','AUD','COP','KMF','CFA','BEA','XAF','CDF','NZD','CRC','HRK','CUP','EUR','CZK','DKK','DJF','XCD','DOP','ECS','EGP','SVC','CFA','BEA','XAF','ERN','EUR','ETB','EUR','FKP','DKK','FJD','EUR','EUR','EUR','EUR','CFA','BEA','XAF','GMD','GEL','EUR','GHS','GIP','GBP','EUR','DKK','XCD','EUR','USA','USD','QTQ','GGP','GNF','GWP','GYD','HTG','AUD','HNL','HKD','HUF','ISK','INR','IDR','IRR','IQD','EUR','GBP','ILS','EUR','CFA','BCE','XOF','JMD','JPY','GBP','JOD','KZT','KES','AUD','KPW','KRW','KWD','KGS','LAK','LVL','LBP','LSL','LRD','LYD','CHF','LTL','EUR','MOP','MKD','MGF','MWK','MYR','MVR','CFA','BCE','XOF','EUR','USD','EUR','MRO','MUR','EUR','MXN','USD','MDL','EUR','MNT','EUR','XCD','MAD','MZN','MMK','NAD','AUD','NPR','EUR','ANG','CFP','XPF','NZD','NIO','CFA','BCE','XOF','NGN','NZD','AUD','USD','NOK','OMR','PKR','USD','PAB','PGK','PYG','PEN','PHP','NZD','PLN','CFP','XPF','EUR','USD','QAR','EUR','RON','RUB','RWF','SHP','XCD','XCD','EUR','XCD','WST','EUR','STD','SAR','CFA','BCE','XOF','RSD','SCR','SLL','SGD','EUR','EUR','SBD','SOS','ZAR','GBP','SSP','EUR','LKR','SDG','SRD','NOK','SZL','SEK','CHF','SYP','TWD','TJS','TZS','THB','CFA','BCE','XOF','NZD','TOP','TTD','TND','TRY','TMT','USD','AUD','GBP','USA','USD','USA','USD','UGX','UAH','AED','UYU','UZS','VUV','EUR','VEF','VND','USD','USA','USD','CFP','XPF','MAD','YER','ZMW','ZWD')
