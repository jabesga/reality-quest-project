from django.db import models


class NPC(models.Model):
    name = models.CharField(max_length=128, default='')
    portrait_style = models.IntegerField(max_length=128, default=0)

    lat = models.FloatField(max_length=128, default=0)
    lng = models.FloatField(max_length=128, default=0)

    def __unicode__(self):
        return self.name


class Quote(models.Model):
    npc = models.ForeignKey(NPC)
    quote = models.CharField(max_length=128, default='What\'s up?')

    def __unicode__(self):
        return "Quote from " + self.npc.name


class Mission(models.Model):
    name = models.CharField(max_length=128, default='')
    mission_briefing = models.CharField(max_length=128, default='')

    start_with = models.ForeignKey(NPC, related_name='start_with')
    start_quote = models.CharField(max_length=128, default='')

    end_with = models.ForeignKey(NPC, related_name='end_with')
    end_quote = models.CharField(max_length=128, default='')

    def __unicode__(self):
        return self.name