from django import forms
from homepage.models import Donation

class PostForm(forms.Form):
    def donations():
        all_donation = Donation.objects.all()
        result = []
        for i in all_donation:
            temp = (f"{i.title}",f"{i.title}")
            result.append(temp)
        
        return result

    message = forms.CharField(label="Your Message", widget=forms.Textarea)
    donation_name = forms.ChoiceField(choices = donations())
    # Add attr class
    message.widget.attrs.update({'class':'bg-gray-200 appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-brokenwhite focus:border-green-medium',
                                'required':'required',
                                'id' : 'id_message',
                                'name' : 'message'
                                })
    donation_name.widget.attrs.update({'class':'col-span-2 form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none',
                                'required':'required',
                                })
