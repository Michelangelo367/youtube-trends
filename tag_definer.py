import pickle

# tags can change over time, as defined by Google.
# this script can be easily altered to match new tags.

tag_definitions = {
    "/m/04rlf": "Music (parent topic)",
    "/m/02mscn": "Christian music",
    "/m/0ggq0m": "Classical music",
    "/m/01lyv": "Country",
    "/m/02lkt": "Electronic music",
    "/m/0glt670": "Hip hop music",
    "/m/05rwpb": "Independent music",
    "/m/03_d0": "Jazz",
    "/m/028sqc": "Music of Asia",
    "/m/0g293": "Music of Latin America",
    "/m/064t9": "Pop music",
    "/m/06cqb": "Reggae",
    "/m/06j6l": "Rhythm and blues",
    "/m/06by7": "Rock music",
    "/m/0gywn": "Soul music",
    "/m/0bzvm2": "Gaming (parent topic)",
    "/m/025zzc": "Action game",
    "/m/02ntfj": "Action-adventure game",
    "/m/0b1vjn": "Casual game",
    "/m/02hygl": "Music video game",
    "/m/04q1x3q": "Puzzle video game",
    "/m/01sjng": "Racing video game",
    "/m/0403l3g": "Role-playing video game",
    "/m/021bp2": "Simulation video game",
    "/m/022dc6": "Sports game",
    "/m/03hf_rm": "Strategy video game",
    "/m/06ntj": "Sports (parent topic)",
    "/m/0jm_": "American football",
    "/m/018jz": "Baseball",
    "/m/018w8": "Basketball",
    "/m/01cgz": "Boxing",
    "/m/09xp_": "Cricket",
    "/m/02vx4": "Football",
    "/m/037hz": "Golf",
    "/m/03tmr": "Ice hockey",
    "/m/01h7lh": "Mixed martial arts",
    "/m/0410tth": "Motorsport",
    "/m/066wd": "Professional wrestling",
    "/m/0f2f9": "TV shows",
    "/m/07bs0": "Tennis",
    "/m/07_53": "Volleyball",
    "/m/02jjt": "Entertainment",
    "/m/095bb": "Animated cartoon",
    "/m/09kqc": "Humor",
    "/m/02vxn": "Movies",
    "/m/05qjc": "Performing arts",
    "/m/019_rr": "Lifestyle",
    "/m/032tl": "Fashion",
    "/m/027x7n": "Fitness",
    "/m/02wbm": "Food",
    "/m/0kt51": "Health",
    "/m/03glg": "Hobby",
    "/m/068hy": "Pets",
    "/m/041xxh": "Physical attractiveness [Beauty]",
    "/m/07c1v": "Technology",
    "/m/07bxq": "Tourism",
    "/m/07yv9": "Vehicles",
    "/m/01k8wb": "Knowledge",
    "/m/098wr": "Society (parent topic)",
    "/m/09s1f": "Business",
    "/m/01h6rj": "Military",
    "/m/05qt0": "Politics",
    "/m/06bvp": "Religion",
    "/m/01k8wb": "Knowledge",
}


def save_pkl(data, name):
    with open(name + ".pkl", "wb") as f:
        pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)


def main():
    save_pkl(tag_definitions, "tag_definitions")
    print("Tag definitions saved...")


if __name__ == "__main__":
    main()