from django.shortcuts import render


def home(request):
    """
    Vista principal que muestra la portada del proyecto con acceso 
    a todas las hojas de vida del equipo.
    """
    hojas_de_vida = [
        {
            "nombre": "Hoja de vida de Jesús",
            "autor": "Jesús",
            "url": "/jesus/",
            "descripcion": "Profesional en desarrollo de software"
        },
        {
            "nombre": "Hoja de vida de Diery",
            "autor": "Diery",
            "url": "/diery/",
            "descripcion": "Desarrolladora con enfoque en web y análisis"
        },
        {
            "nombre": "Hoja de vida de Nicolás",
            "autor": "Nicolás",
            "url": "/nicolas/",
            "descripcion": "Desarrollador especializado en tecnologías modernas"
        },
        {
            "nombre": "Hoja de vida de Oskar",
            "autor": "Oskar",
            "url": "/oskar/",
            "descripcion": "Profesional en ingeniería de software"
        },
    ]
    
    context = {
        'hojas_de_vida': hojas_de_vida,
        'total_integrantes': len(hojas_de_vida),
    }
    
    return render(request, 'home.html', context)
