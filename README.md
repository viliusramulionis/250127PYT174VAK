# 250127PYT174VAK Paskaitų medžiaga

.gitignore - Faile įrašome failų ir direktorijų pavadinimus kurių nenorime talpinti

# GIT komandos talpinant NAUJĄ repozitoriją:

    git init - Naujos repozitorijus inciavimas

    git add . - Pridedame naujus failus prie "stage" fazės (taškas reiškią esamą direktoriją, vietoje jo galima vardinti failų ir direktorijų pavadinimus)

    git commit -m "Pridedama žinutė prie commit'o" - Žinutės priskyrimas

    git branch -M main - Atšakos sukūrimo nurodymas

    git remote add origin REPOZITORIJOS ADRESAS - Sukurtos github repozitorijos adreso pridėjimas

    git push -u origin main - Failų perkėlimo nurodymas

# GIT repozitorijos atnaujinimų komandos:

    git add . - Nurodome norimus pridėti failus

    git commit -m "Nurodome atnaujinimo paskirtį" - Commit'o priskyrimas su žinute

    git push - Pakeitimų perkėlimas

# Repozitorijos klonavimas:

    git clone REPOZITORIJOS_ADRESAS

# Repozitorijos pakeitimų atsiuntimas

    git pull

# Repozitorijos atšakų (branches) kūrimas

    git branch PAVADINIMAS - Nurodome atšakos inciavimą

    git checkout PAVADINIMAS - Pereiname į naujai sukurtą atšaką

    git push --set-upstream origin PAVADINIMAS - Perkeliame pakeitimus 


# Repozitorijos atšakų sujungimas

    git checkout BRANCHAS_I_KURI_PERKELIAME_DUOMENIS

    git merge BRANCHAS_IS_KURIO_IMAME_DUOMENIS

    git push

# Failų trynimas iš repozitorijos atšakos

    git rm -rf . - rm nurodo trynimo iniciavimą, -rf nurodo, jog jeigu triname direktoriją, būtų pašalinti vidiniai failai, o taškas nurodo ką triname

# PyQt6 aplikacijos direktorijos paruošimas

VS code atsidarome norimą aplanką kuriame dirbsime. Aktyvuojame virtualią aplinką su komanda:

    py -m venv venv
    call venv/Scripts/activate.bat 

    ARBA

    source venv/bin/activate

Instaliuojame biblioteką:

    pip install PyQt6

PyQt6 Dizainerio failo konvertavimas:

    py -m PyQt6.uic.pyuic FAILO_PAVADINIMAS -o PYTHON_FAILO_PAVADINIMAS


