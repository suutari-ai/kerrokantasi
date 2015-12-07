from django.contrib import admin
from django.db.models import TextField
from django.utils.translation import ugettext_lazy as _
from nested_admin.nested import NestedAdmin, NestedStackedInline

from democracy import models
from democracy.admin.widgets import ShortTextAreaWidget


# Inlines


class HearingImageInline(NestedStackedInline):
    model = models.HearingImage
    extra = 0
    exclude = ("public", "title")
    formfield_overrides = {
        TextField: {'widget': ShortTextAreaWidget}
    }


class SectionImageInline(NestedStackedInline):
    model = models.SectionImage
    extra = 0
    exclude = ("public", "title")
    formfield_overrides = {
        TextField: {'widget': ShortTextAreaWidget}
    }


class SectionInline(NestedStackedInline):
    model = models.Section
    extra = 1
    inlines = [SectionImageInline]
    exclude = ("public", "commenting",)
    formfield_overrides = {
        TextField: {'widget': ShortTextAreaWidget}
    }


# Admins


class HearingAdmin(NestedAdmin):
    inlines = [HearingImageInline, SectionInline]
    list_display = ("id", "published", "title", "open_at", "close_at", "force_closed")
    list_filter = ("published",)
    search_fields = ("id", "title")
    fieldsets = (
        (None, {
            "fields": ("title", "abstract", "labels", "id")
        }),
        (_("Availability"), {
            "fields": ("published", "open_at", "close_at", "force_closed", "commenting")
        }),
    )
    formfield_overrides = {
        TextField: {'widget': ShortTextAreaWidget}
    }

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        hearing = form.instance
        assert isinstance(hearing, models.Hearing)
        hearing.sections.update(commenting=hearing.commenting)


class LabelAdmin(admin.ModelAdmin):
    exclude = ("public",)


# Wire it up!


admin.site.register(models.Label, LabelAdmin)
admin.site.register(models.Hearing, HearingAdmin)
