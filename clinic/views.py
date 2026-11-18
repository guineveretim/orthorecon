from django.shortcuts import render
from django.http import Http404

def home(request):
    return render(request, 'clinic/home.html')
def about(request):
    return render(request, 'clinic/about.html')
def services(request):
    return render(request, 'clinic/services.html')
def patient_info(request):
    return render(request, 'clinic/patient_info.html')
def referrals(request):
    return render(request, 'clinic/referrals.html')
def research(request):
    return render(request, 'clinic/research.html')
def faq(request):
    return render(request, 'clinic/faq.html')
def contact(request):
    return render(request, 'clinic/contact.html')

SERVICES = {
   'hip-replacement': {
    'title': 'Hip Replacement',
    'tagline': 'For arthritis and hip fractures. Return to walking pain-free.',
    'what': 'Hip replacement replaces the damaged ball-and-socket joint with a metal and plastic implant. It removes arthritis pain and restores movement.',
    'for_who': ['Severe hip arthritis', 'Hip fractures in older patients', 'Avascular necrosis (bone death)', 'Failed previous hip surgery'],
    'happens': ['Consult + X-ray / CT scan', 'Surgery: 1.5 - 2 hours', 'Hospital: 2-3 days', 'Walking same day with physio', 'Full recovery: 6-12 weeks'],
    'model_type': 'hip',
    'sketchfab': 'https://sketchfab.com/models/d563832690dc4f82a789096474060712/embed',
    'credit': 'HumanX Medical Simulators',
},
    'knee-replacement': {
        'title': 'Knee Replacement',
        'tagline': 'Total and partial knee replacement for severe arthritis.',
        'what': 'Knee replacement resurfaces the worn ends of the thigh and shin bone with metal and plastic, giving you a smooth, pain-free knee.',
        'for_who': ['Severe knee arthritis', 'Bowed leg / deformity', 'Knee pain at night', 'Failed injections / physio'],
        'happens': ['Consult + X-ray', 'Surgery: 1.5 - 2 hours', 'Hospital: 2-3 days', 'Physio starts day 1', 'Full recovery: 3-6 months'],
        'model_type': 'knee',
    },
    'pelvic-acetabular': {
        'title': 'Pelvic & Acetabular Reconstruction',
        'tagline': 'Specialist reconstruction for pelvic fractures.',
        'what': 'Complex pelvic fractures need specialist fixation to restore the ring of the pelvis, protect organs, and let you walk again.',
        'for_who': ['Pelvic fractures from road accidents', 'Acetabular (hip socket) fractures', 'Pelvic non-unions', 'Complex pelvic deformity'],
        'happens': ['Emergency assessment + CT', 'Specialist surgical planning', 'Surgery: 2-4 hours', 'Hospital: 3-5 days', 'Rehab: 3-6 months with physio'],
        'model_type': 'pelvis',
    },
    'complex-trauma': {
        'title': 'Complex Trauma',
        'tagline': 'Complex fractures, non-unions and polytrauma.',
        'what': 'For fractures that are broken into many pieces, infected, or did not heal before. We rebuild the bone and restore alignment.',
        'for_who': ['Multiple fractures', 'Open fractures', 'Fractures that did not heal (non-union)', 'Infected fractures'],
        'happens': ['Assessment + X-ray / CT', 'Stabilisation if needed', 'Definitive fixation surgery', 'Follow-up + physio plan', 'Healing: 3-9 months depending on injury'],
        'model_type': 'trauma',
    },
    'adult-reconstruction': {
        'title': 'Adult Reconstruction',
        'tagline': 'Degenerative joint disease and revision surgery.',
        'what': 'When a previous joint replacement wears out, loosens or gets infected, revision surgery replaces it with a new implant.',
        'for_who': ['Worn out hip / knee replacement', 'Loose or painful implant', 'Infected joint replacement', 'Severe arthritis in younger patients'],
        'happens': ['Consult + X-ray / CT', 'Planning + implant selection', 'Surgery: 2-3 hours', 'Hospital: 3-4 days', 'Recovery: 3-6 months'],
        'model_type': 'hip',
    },
    'fracture-care': {
        'title': 'Fracture Care',
        'tagline': 'Structured follow-up and rehab guidance.',
        'what': 'Not every fracture needs surgery. We assess, treat, and follow you until the bone is healed and you are back to normal.',
        'for_who': ['Fresh fractures', 'Stress fractures', 'Fractures in children / elderly', 'Follow-up after surgery elsewhere'],
        'happens': ['Assessment + X-ray', 'Plaster / brace or surgery if needed', 'Follow-up X-rays', 'Physio + rehab guidance', 'Return to work / sport plan'],
        'model_type': 'trauma',
    },
}

def service_detail(request, slug):
    service = SERVICES.get(slug)
    if not service:
        raise Http404("Service not found")
    return render(request, 'clinic/service_detail.html', {'service': service, 'slug': slug})