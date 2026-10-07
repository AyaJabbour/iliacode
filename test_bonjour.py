from bonjour import saluer
def test_saluer_asmaa():
    assert saluer("Aya") == "Bonjour Aya"
def test_saluer_vide():
    assert saluer("") == "Bonjour "