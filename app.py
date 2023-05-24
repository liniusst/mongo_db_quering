# pylint: disable= missing-docstring
import tkinter as tk
from task import generate, update_collection
from database import get_db, create_collection


# tk lango nustatymai
root = tk.Tk()
root.geometry("750x270")
root.title("Generate Database query")

# data lauku reiksmes, kur int reiksmes uzsetiname IntVar
database_name_label = tk.Label(root, text="Database name:")
database_name_entry = tk.Entry(root)
collecction_name_label = tk.Label(root, text="Collection name:")
colletion_name_entry = tk.Entry(root)
field_name_label = tk.Label(root, text="Field name:")
field_name_entry = tk.Entry(root)
field_type_label = tk.Label(root, text="Field type:")
field_type_entry = tk.Entry(root)
range_min_label = tk.Label(root, text="Range(min):")
range_min_int = tk.IntVar()
range_min_entry = tk.Entry(root, textvariable=range_min_int)
range_max_label = tk.Label(root, text="Range(max):")
range_max_int = tk.IntVar()
range_max_entry = tk.Entry(root, textvariable=range_max_int)
need_doc_label = tk.Label(root, text="Documents num:")
need_doc_int = tk.IntVar()
need_doc_entry = tk.Entry(root, textvariable=need_doc_int)


# sudeliojam lango front
database_name_label.grid(row=0, column=0, sticky="e", pady=10, padx=10)
database_name_entry.grid(row=0, column=1)
collecction_name_label.grid(row=0, column=2, sticky="e", pady=10, padx=10)
colletion_name_entry.grid(row=0, column=3)
field_name_label.grid(row=1, column=0, sticky="e", pady=10, padx=10)
field_name_entry.grid(row=1, column=1)
field_type_label.grid(row=1, column=2, sticky="e")
field_type_entry.grid(row=1, column=3)
range_min_label.grid(row=2, column=0, sticky="e", pady=10, padx=10)
range_min_entry.grid(row=2, column=1)
range_max_label.grid(row=2, column=2, sticky="e")
range_max_entry.grid(row=2, column=3)
need_doc_label.grid(row=3, column=0, sticky="e", pady=10, padx=10)
need_doc_entry.grid(row=3, column=1)


# nustatom mygtuku reiksmes, lambda kad is karto nekviestu
create_db_button = tk.Button(
    root, text="Create DB", command=lambda: get_db(database_name_entry.get())
)

create_coll_button = tk.Button(
    root,
    text="Create Collection",
    command=lambda: create_collection(
        database_name_entry.get(),
        colletion_name_entry.get(),
    ),
)
generate_button = tk.Button(
    root,
    text="Generate",
    command=lambda: generate(
        database_name_entry,
        colletion_name_entry,
        need_doc_entry,
        field_type_entry,
        field_name_entry,
        range_min_entry,
        range_max_entry,
    ),
)
update_button = tk.Button(
    root,
    text="Update collection all docs",
    command=lambda: update_collection(
        database_name_entry,
        colletion_name_entry,
        field_type_entry,
        field_name_entry,
        range_min_entry,
        range_max_entry,
    ),
)


# sudedam mygtuku isdestyma gride
create_db_button.grid(row=4, column=0, pady=15)
create_coll_button.grid(row=4, column=1, pady=15)
generate_button.grid(row=4, column=2, pady=15)
update_button.grid(row=4, column=3, pady=15)


root.mainloop()
