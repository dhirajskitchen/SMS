from data.load_data import load_students, load_classes

def view_all_students():
    students_df = load_students()
    classes_df = load_classes()

    students_df = students_df.sort_values(['class_id', 'student_id'])

    class_lookup = (
        classes_df
        .set_index('class_id')[['class_grade', 'section']]
        .to_dict('index')
    )

    print(f"{'ID':<10} {'Name':<25} {'Class':<10}")
    print("-" * 50)

    for _, row in students_df.iterrows():
        class_info = class_lookup.get(row['class_id'])

        if class_info:
            class_name = f"{class_info['class_grade']}-{class_info['section']}"
        else:
            class_name = "Unknown"

        print(
            f"{row['student_id']:<10} "
            f"{row['name']:<25} "
            f"{class_name:<10}"
        )