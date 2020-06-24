from interactions.models import SelfAnswerGroup


def clean_multiple_results_data(master_pk: int, *primary_keys: list):
    primary_keys = list(
        int(primary_key) for
        primary_key in primary_keys if primary_key.strip().isdigit()
    )
    primary_keys.append(master_pk.pk)
    valid_pks, unavailable_pks, duplicate_pks = set(), set(), set()
    for primary_key in primary_keys:
        if primary_key in [
            ans_gp['pk'] for ans_gp in SelfAnswerGroup.objects.values('pk')
        ]:
            if primary_key not in valid_pks:
                valid_pks.add(primary_key)
            else:
                duplicate_pks.add(primary_key)
        else:
            if primary_key not in unavailable_pks:
                unavailable_pks.add(primary_key)
            else:
                duplicate_pks.add(primary_key)

    another = list()
    for pk in valid_pks:
        ans_gp = SelfAnswerGroup.objects.get(pk=pk)
        master_bool = True if pk is int(master_pk.pk) else False
        another.append({
            'name': ans_gp.user_profile.user.username,
            'master': master_bool,
            'answer_group_pk': pk
        })

    return another, unavailable_pks, duplicate_pks


def process_valid_dict(valid_dict: list) -> list:
	if len(valid_dict) <= 2:
		return [valid_dict] 
	else:
		cleaned = []
		for index, dictionary in enumerate(valid_dict):
			cleaner = []
			cleaner.append(valid_dict[index:index+2])
			cleaned.append(cleaner)
		
		return cleaned
		