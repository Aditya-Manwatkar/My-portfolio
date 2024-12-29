from django.shortcuts import render, get_object_or_404
from django.template.defaulttags import register
from .models import Project, Skill, Education, Internship, Experience, Contribution, CocurricularActivity, ResearchBlog, Thought, SocialProfile

register.filter('multiply', lambda value, arg: value * arg)

def home(request):
    projects = Project.objects.all().order_by('-created_at')[:3]
    skills = Skill.objects.all().order_by('-proficiency')
    education = Education.objects.all().order_by('-end_date')
    internships = Internship.objects.all().order_by('-end_date')
    experiences = Experience.objects.all().order_by('-end_date')
    contributions = Contribution.objects.all()
    cocurricular_activities = CocurricularActivity.objects.all().order_by('-date')
    research_blogs = ResearchBlog.objects.all().order_by('-publication_date')
    thoughts = Thought.objects.all().order_by('-date')[:5]  # Display only the 5 most recent thoughts
    social_profiles = SocialProfile.objects.all()

    return render(request, 'portfolio/home.html', {
        'projects': projects,
        'skills': skills,
        'education': education,
        'internships': internships,
        'experiences': experiences,
        'contributions': contributions,
        'cocurricular_activities': cocurricular_activities,
        'research_blogs': research_blogs,
        'thoughts': thoughts,
        'social_profiles': social_profiles,
    })

def projects(request):
    projects = Project.objects.all().order_by('-created_at')
    return render(request, 'portfolio/projects.html', {'projects': projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'portfolio/project_detail.html', {'project': project})

