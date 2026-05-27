from django.shortcuts import render

# Create your views here.
@property
def education_status(self):

    if not self.has_formal_education:
        return "never_educated"

    if not self.education.exists():
        return "unknown"

    if self.education.filter(status="ongoing").exists():
        return "studying"

    return "educated"