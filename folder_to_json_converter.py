
import json
import os

def folder_to_json(folder_path):
    result = []

    # Process Modules
    for module_name in os.listdir(folder_path):
        module_path = os.path.join(folder_path, module_name)
        if os.path.isdir(module_path):
            with open(os.path.join(module_path, "info.json"), "r") as file:
                module_info = json.load(file)
            module_pk = int(module_name.split('_')[1])
            result.append({
                "model": "videos.module",
                "pk": module_pk,
                "fields": {
                    "name": module_info['name'],
                    "description": module_info['description'],
                    "order": module_pk
                }
            })

            # Process SubModules for each Module
            for submodule_name in os.listdir(module_path):
                submodule_path = os.path.join(module_path, submodule_name)
                if os.path.isdir(submodule_path):
                    with open(os.path.join(submodule_path, "info.json"), "r") as file:
                        submodule_info = json.load(file)
                    submodule_pk = int(submodule_name.split('_')[1])
                    result.append({
                        "model": "videos.submodule",
                        "pk": submodule_pk,
                        "fields": {
                            "name": submodule_info['name'],
                            "description": submodule_info['description'],
                            "module": module_pk,
                            "order": submodule_pk
                        }
                    })

                    # Process Topics for each SubModule
                    for topic_name in os.listdir(submodule_path):
                        topic_path = os.path.join(submodule_path, topic_name)
                        if os.path.isdir(topic_path):
                            with open(os.path.join(topic_path, "info.json"), "r") as file:
                                topic_info = json.load(file)
                            topic_pk = int(topic_name.split('_')[1])
                            result.append({
                                "model": "videos.topic",
                                "pk": topic_pk,
                                "fields": {
                                    "name": topic_info['name'],
                                    "description": topic_info['description'],
                                    "submodule": submodule_pk,
                                    "order": topic_pk
                                }
                            })

                            # Videos for each Topic
                            with open(os.path.join(topic_path, "videos.json"), "r") as file:
                                videos = json.load(file)
                            result.extend(videos)

                            # CourseNotes for each Topic
                            with open(os.path.join(topic_path, "notes.md"), "r") as file:
                                notes = file.read().split("\n\n")
                            for idx, note in enumerate(notes):
                                result.append({
                                    "model": "videos.coursenote",
                                    "fields": {
                                        "topic": topic_pk,
                                        "content": note,
                                        "order": idx
                                    }
                                })

                            # AdditionalLinks for each Topic
                            with open(os.path.join(topic_path, "links.json"), "r") as file:
                                links = json.load(file)
                            result.extend(links)

    return result


def json_to_folder(json_path, folder_path):
    # Load the JSON data
    with open(json_path, "r") as file:
        data = json.load(file)

    # Base content directory
    os.makedirs(folder_path, exist_ok=True)

    # Process Modules
    for module in [item for item in data if item['model'] == 'videos.module']:
        module_dir = os.path.join(folder_path, f"module_{module['pk']}")
        os.makedirs(module_dir, exist_ok=True)
        with open(os.path.join(module_dir, "info.json"), "w") as file:
            json.dump({
                "name": module['fields']['name'],
                "description": module['fields']['description']
            }, file, indent=4)

        # Process SubModules for each Module
        for submodule in [item for item in data if item['model'] == 'videos.submodule' and item['fields']['module'] == module['pk']]:
            submodule_dir = os.path.join(module_dir, f"submodule_{submodule['pk']}")
            os.makedirs(submodule_dir, exist_ok=True)
            with open(os.path.join(submodule_dir, "info.json"), "w") as file:
                json.dump({
                    "name": submodule['fields']['name'],
                    "description": submodule['fields']['description']
                }, file, indent=4)

            # Process Topics for each SubModule
            for topic in [item for item in data if item['model'] == 'videos.topic' and item['fields']['submodule'] == submodule['pk']]:
                topic_dir = os.path.join(submodule_dir, f"topic_{topic['pk']}")
                os.makedirs(topic_dir, exist_ok=True)
                with open(os.path.join(topic_dir, "info.json"), "w") as file:
                    json.dump({
                        "name": topic['fields']['name'],
                        "description": topic['fields']['description']
                    }, file, indent=4)

                # Videos for each Topic
                videos = [item for item in data if item['model'] == 'videos.video' and item['fields']['topic'] == topic['pk']]
                with open(os.path.join(topic_dir, "videos.json"), "w") as file:
                    json.dump(videos, file, indent=4)

                # CourseNotes for each Topic
                notes = [item['fields']['content'] for item in data if item['model'] == 'videos.coursenote' and item['fields']['topic'] == topic['pk']]
                with open(os.path.join(topic_dir, "notes.md"), "w") as file:
                    file.write("\n\n".join(notes))

                # AdditionalLinks for each Topic
                links = [item for item in data if item['model'] == 'videos.additionallink' and item['fields']['topic'] == topic['pk']]
                with open(os.path.join(topic_dir, "links.json"), "w") as file:
                    json.dump(links, file, indent=4)


# Uncomment the following lines based on your needs:

# To generate a Django-compatible JSON dump from the folder structure:
# result = folder_to_json("/path/to/folder")
# with open("/path/to/output.json", "w") as file:
#     json.dump(result, file, indent=4)

# To generate the folder structure from a Django-compatible JSON dump:
json_to_folder("/Users/patrik/Repos/practical-bug-bounty/bugbountytube/test.json", "/Users/patrik/Repos/practical-bug-bounty-content/content/")
