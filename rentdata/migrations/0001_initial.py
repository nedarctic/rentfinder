# Generated by Django 5.1.3 on 2024-11-10 19:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')], default='TX', max_length=2)),
                ('apartment_type', models.CharField(choices=[('Studio', 'Studio'), ('1BR', '1 Bedroom'), ('2BR', '2 Bedroom'), ('3BR', '3 Bedroom'), ('Other', 'Other')], max_length=50)),
                ('amenities', models.CharField(blank=True, choices=[('GYM', 'Gym'), ('POOL', 'Swimming Pool'), ('PARK', 'Parking'), ('WASHER', 'Washer/Dryer'), ('AC', 'Air Conditioning'), ('HEAT', 'Central Heating'), ('BALCONY', 'Balcony'), ('PET_FRIENDLY', 'Pet Friendly'), ('ELEVATOR', 'Elevator'), ('SECURITY', 'Security System'), ('SMOKE_FREE', 'Smoke Free')], max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RentData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('income_bracket', models.IntegerField(choices=[(10000, 'Up to $10,000'), (20000, 'Up to $20,000'), (30000, 'Up to $30,000'), (40000, 'Up to $40,000'), (50000, 'Up to $50,000'), (60000, 'Up to $60,000'), (70000, 'Up to $70,000'), (80000, 'Up to $80,000'), (100000, 'Up to $100,000'), (200000, 'Up to $200,000'), (300000, 'Up to $300,000'), (500000, 'Up to $500,000')])),
                ('rent_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('lease_start_date', models.DateField()),
                ('lease_end_date', models.DateField(blank=True, null=True)),
                ('rent_paid_date', models.DateField(auto_now_add=True)),
                ('apartment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rent_data', to='rentdata.apartment')),
            ],
        ),
    ]
