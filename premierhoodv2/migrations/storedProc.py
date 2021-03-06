from django.db import migrations

SQL = """CREATE PROCEDURE add_count(player_id int) 
    AS $$
    BEGIN
	    UPDATE premierhoodv2_player 
        SET  buyCount = buyCount + 1
        WHERE id = player_id;
        COMMIT;
    END;
    $$
    LANGUAGE PLPGSQL;
    """
class Migration(migrations.Migration):
    dependencies = [
        ('premierhoodv2', '0002_auto_20211217_2223'),
    ]

    operations = [migrations.RunSQL(SQL)]
