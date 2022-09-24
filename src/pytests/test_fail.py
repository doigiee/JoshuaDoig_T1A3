import pytest
@pytest.fixture
def Blob():
	fire = 25
	water = 35
	grass = 45
	return [fire,water,grass]

def test_comparewithfire(Blob):
	mylevel=35
	assert Blob[0]==mylevel,"fire and mylevel comparison failed"

def test_comparewithwater(Blob):
	mylevel=35
	assert Blob[1]==mylevel,"water and mylevel comparison failed"

def test_comparewithgrass(Blob):
	mylevel=35
	assert Blob[2]==mylevel,"grass and mylevel comparison failed"

