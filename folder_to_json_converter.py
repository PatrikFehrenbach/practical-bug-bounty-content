import os
import json

CONTENT_DIR = "/Users/patrik/Repos/practical-bug-bounty-content/content/"

def json_to_folder(json_filepath, output_folder=CONTENT_DIR):
    """
    Convert the given Django-style JSON dump into the folder structure.
    """
    # Load the JSON data
    with open(json_filepath, 'r') as json_file:
        json_data = json.load(json_file)

    # Create dictionaries to store models
    modules_dict = {}
    submodules_dict = {}
    topics_dict = {}

    # Organize data
    for entry in json_data:
        if entry['model'] == "videos.module":
            modules_dict[entry['pk']] = entry['fields']

        elif entry['model'] == "videos.submodule":
            submodules_dict[entry['pk']] = entry['fields']

        elif entry['model'] == "videos.topic":
            topics_dict[entry['pk']] = entry['fields']

    # Process Modules
    for module_id, module_fields in modules_dict.items():
        module_folder = os.path.join(output_folder, module_fields['name'])
        os.makedirs(module_folder, exist_ok=True)
        with open(os.path.join(module_folder, 'info.json'), 'w') as f:
            json.dump({'description': module_fields['description']}, f, indent=4)

        # Process SubModules
        for submodule_id, submodule_fields in submodules_dict.items():
            if submodule_fields['module'] == module_id:
                submodule_folder = os.path.join(module_folder, submodule_fields['name'])
                os.makedirs(submodule_folder, exist_ok=True)
                with open(os.path.join(submodule_folder, 'info.json'), 'w') as f:
                    json.dump({'description': submodule_fields['description']}, f, indent=4)

                # Process Topics
                for topic_id, topic_fields in topics_dict.items():
                    if topic_fields['submodule'] == submodule_id:
                        topic_folder = os.path.join(submodule_folder, topic_fields['name'])
                        os.makedirs(topic_folder, exist_ok=True)
                        with open(os.path.join(topic_folder, 'info.json'), 'w') as f:
                            json.dump({'description': topic_fields['description']}, f, indent=4)

                        # Process Videos
                        for entry in json_data:
                            if entry['model'] == "videos.video" and entry['fields']['topic'] == topic_id:
                                video = {
                                    'title': entry['fields']['title'],
                                    'url': entry['fields']['url'],
                                    'tags': entry['fields']['tags'],
                                }
                                videos = []
                                if os.path.exists(os.path.join(topic_folder, 'videos.json')):
                                    with open(os.path.join(topic_folder, 'videos.json'), 'r') as f:
                                        videos = json.load(f)
                                videos.append(video)
                                with open(os.path.join(topic_folder, 'videos.json'), 'w') as f:
                                    json.dump(videos, f, indent=4)

                        # Process Course Notes
                        for entry in json_data:
                            if entry['model'] == "videos.coursenote" and entry['fields']['topic'] == topic_id:
                                with open(os.path.join(topic_folder, 'notes.md'), 'a') as f:
                                    f.write(entry['fields']['content'] + '\n\n')

                        # Process Additional Links
                        for entry in json_data:
                            if entry['model'] == "videos.additionallink" and entry['fields']['topic'] == topic_id:
                                additional_link = {
                                    'url': entry['fields']['url'],
                                    'description': entry['fields']['description']
                                }
                                additional_links = []
                                if os.path.exists(os.path.join(topic_folder, 'links.json')):
                                    with open(os.path.join(topic_folder, 'links.json'), 'r') as f:
                                        additional_links = json.load(f)
                                additional_links.append(additional_link)
                                with open(os.path.join(topic_folder, 'links.json'), 'w') as f:
                                    json.dump(additional_links, f, indent=4)


def folder_to_json_with_pks(folder_path=CONTENT_DIR):
    """
    Convert the folder structure back to Django-style JSON dump.
    """
    data = []

    module_pk = 1
    submodule_pk = 1
    topic_pk = 1
    video_pk = 1
    note_pk = 1
    link_pk = 1

    # List all modules
    for module_name in os.listdir(folder_path):
        module_path = os.path.join(folder_path, module_name)
        if os.path.isdir(module_path):
            with open(os.path.join(module_path, 'info.json'), 'r') as f:
                module_info = json.load(f)
            
            module_data = {
                'model': 'videos.module',
                'pk': module_pk,
                'fields': {
                    'name': module_name,
                    'description': module_info.get('description', ''),
                }
            }
            data.append(module_data)

            # List all submodules for the current module
            for submodule_name in os.listdir(module_path):
                submodule_path = os.path.join(module_path, submodule_name)
                if os.path.isdir(submodule_path):
                    with open(os.path.join(submodule_path, 'info.json'), 'r') as f:
                        submodule_info = json.load(f)
                    
                    submodule_data = {
                        'model': 'videos.submodule',
                        'pk': submodule_pk,
                        'fields': {
                            'name': submodule_name,
                            'description': submodule_info.get('description', ''),
                            'module': module_pk
                        }
                    }
                    data.append(submodule_data)

                    # List all topics for the current submodule
                    for topic_name in os.listdir(submodule_path):
                        topic_path = os.path.join(submodule_path, topic_name)
                        if os.path.isdir(topic_path):
                            with open(os.path.join(topic_path, 'info.json'), 'r') as f:
                                topic_info = json.load(f)
                            
                            topic_data = {
                                'model': 'videos.topic',
                                'pk': topic_pk,
                                'fields': {
                                    'name': topic_name,
                                    'description': topic_info.get('description', ''),
                                    'submodule': submodule_pk
                                }
                            }
                            data.append(topic_data)
                            
                            # Handle videos
                            with open(os.path.join(topic_path, 'videos.json'), 'r') as f:
                                videos = json.load(f)
                            
                            for video in videos:
                                video_data = {
                                    'model': 'videos.video',
                                    'pk': video_pk,
                                    'fields': {
                                        'title': video['title'],
                                        'url': video['url'],
                                        'tags': video.get('tags', ''),
                                        'topic': topic_pk
                                    }
                                }
                                data.append(video_data)
                                video_pk += 1
                            
                            # Handle notes
                            notes_filepath = os.path.join(topic_path, 'notes.md')
                            if os.path.exists(notes_filepath):
                                with open(notes_filepath, 'r') as f:
                                    notes = f.read()
                                
                                if notes.strip():
                                    note_data = {
                                        'model': 'videos.coursenote',
                                        'pk': note_pk,
                                        'fields': {
                                            'topic': topic_pk,
                                            'content': notes.strip()
                                        }
                                    }
                                    data.append(note_data)
                                    note_pk += 1
                            else:
                                notes = ''

                            
                            # Handle additional links
                            links_filepath = os.path.join(topic_path, 'links.json')
                            if os.path.exists(links_filepath):
                                with open(links_filepath, 'r') as f:
                                    additional_links = json.load(f)
                                
                                for link in additional_links:
                                    link_data = {
                                        'model': 'videos.additionallink',
                                        'pk': link_pk,
                                        'fields': {
                                            'topic': topic_pk,
                                            'url': link['url'],
                                            'description': link.get('description', '')
                                        }
                                    }
                                    data.append(link_data)
                                    link_pk += 1
                            else:
                                additional_links = []
                            
                            topic_pk += 1
                    submodule_pk += 1
            module_pk += 1

    return data
if __name__ == "__main__":
    # Example usage
    # Convert Django-style JSON dump to folder structure
#    json_to_folder("/Users/patrik/Repos/practical-bug-bounty/bugbountytube/test.json", "/Users/patrik/Repos/practical-bug-bounty-content/content/")

    # Convert folder structure back to Django-style JSON dump
    converted_data = folder_to_json_with_pks()
    with open("/Users/patrik/Repos/practical-bug-bounty/bugbountytube/output.json", 'w') as f:
        json.dump(converted_data, f, indent=4)
