from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import ContactInquiry, CourseEnquiry, BrochureRequest, PlacedStudent, Trainer, Course, Career, JobApplication

# Customizing general Admin Site branding
admin.site.site_header = "SDC Networks Admin Portal"
admin.site.site_title = "SDC Networks Admin Portal"
admin.site.index_title = "Inquiries & Brochure Downloads Dashboard"



@admin.register(ContactInquiry)
class ContactInquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'course', 'created_at')
    list_filter = ('course', 'created_at')
    search_fields = ('name', 'email', 'phone', 'message', 'course')
    readonly_fields = ('name', 'email', 'phone', 'course', 'message', 'created_at')
    date_hierarchy = 'created_at'
    
    def has_add_permission(self, request):
        return False


@admin.register(CourseEnquiry)
class CourseEnquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'course', 'created_at')
    list_filter = ('course', 'created_at')
    search_fields = ('name', 'email', 'phone', 'message', 'course')
    readonly_fields = ('name', 'email', 'phone', 'course', 'message', 'created_at')
    date_hierarchy = 'created_at'
    
    def has_add_permission(self, request):
        return False


@admin.register(BrochureRequest)
class BrochureRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'college_or_place', 'course_slug', 'created_at')
    list_filter = ('course_slug', 'created_at')
    search_fields = ('name', 'phone', 'college_or_place', 'course_slug')
    readonly_fields = ('name', 'phone', 'college_or_place', 'course_slug', 'created_at')
    date_hierarchy = 'created_at'
    
    def has_add_permission(self, request):
        return False


@admin.register(PlacedStudent)
class PlacedStudentAdmin(admin.ModelAdmin):
    list_display = ('order', 'id', 'image_preview', 'created_at')
    list_display_links = ('id',)
    list_editable = ('order',)
    list_filter = ('created_at',)
    search_fields = ('id',)
    readonly_fields = ('image_preview_large',)
    
    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="width: 50px; height: 50px; object-fit: cover; border-radius: 5px;" />')
        return "No Image"
    image_preview.short_description = "Photo"

    def image_preview_large(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="max-width: 300px; max-height: 300px; object-fit: contain; border-radius: 10px;" />')
        return "No Image"
    image_preview_large.short_description = "Current Photo"


@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('order', 'name', 'course', 'image_preview', 'created_at')
    list_display_links = ('name',)
    list_editable = ('order',)
    list_filter = ('course', 'created_at')
    search_fields = ('name', 'course')
    readonly_fields = ('image_preview_large',)

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="width: 50px; height: 50px; object-fit: cover; border-radius: 5px;" />')
        return "No Image"
    image_preview.short_description = "Photo"

    def image_preview_large(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="max-width: 300px; max-height: 300px; object-fit: contain; border-radius: 10px;" />')
        return "No Image"
    image_preview_large.short_description = "Current Photo"


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('order', 'title', 'slug', 'category', 'duration', 'level', 'rating', 'image_preview', 'created_at')
    list_display_links = ('title',)
    list_editable = ('order',)
    list_filter = ('category', 'level', 'created_at')
    search_fields = ('title', 'slug', 'description', 'category')
    readonly_fields = ('image_preview_large',)
    filter_horizontal = ('instructors',)

    fieldsets = (
        ('Basic Information', {
            'fields': ('slug', 'title', 'category', 'description', 'order')
        }),
        ('Course Meta', {
            'fields': ('duration', 'level', 'rating')
        }),
        ('Media Settings', {
            'fields': ('image', 'image_preview_large')
        }),
        ('Highlights & Outcomes', {
            'fields': ('highlights', 'outcomes')
        }),
        ('Syllabus & Details', {
            'fields': ('overview', 'syllabus', 'brochure')
        }),
        ('Instructors / Trainers', {
            'fields': ('instructors',)
        }),
    )

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="width: 50px; height: 50px; object-fit: cover; border-radius: 5px;" />')
        return "No Image"
    image_preview.short_description = "Photo"

    def image_preview_large(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="max-width: 300px; max-height: 300px; object-fit: contain; border-radius: 10px;" />')
        return "No Image"
    image_preview_large.short_description = "Current Photo"


@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('title', 'description', 'requirements')


@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'job', 'created_at', 'resume_link')
    list_filter = ('job', 'created_at')
    search_fields = ('name', 'email', 'phone')
    readonly_fields = ('name', 'email', 'phone', 'job', 'resume', 'created_at')
    date_hierarchy = 'created_at'

    def resume_link(self, obj):
        if obj.resume:
            return mark_safe(f'<a href="{obj.resume.url}" target="_blank">View Resume</a>')
        return "No Resume"
    resume_link.short_description = "Resume"
    
    def has_add_permission(self, request):
        return False
