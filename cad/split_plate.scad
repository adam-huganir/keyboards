include<BOSL2/std.scad>

// --- Keyboard layout constants (mm) ---
u = 19.05;                     // Standard key spacing (1u)
switch_hole_width = 14.0;      // MX switch cutout width
switch_hole_height = 14.0;     // MX switch cutout height
plate_switch_clearance = 0.05; // Extra clearance per side

switch_hole_x = switch_hole_width + 2 * plate_switch_clearance;
switch_hole_y = switch_hole_height + 2 * plate_switch_clearance;

epsilon = 0.01;
plate_thickness = 3.0;

// --- Customizer: column Y offsets (mm) ---

n_columns = 6; // [4 : 7]
offset_preset = "custom"; // [custom, corne]


index_far_y = 0; // [-15:15]
index_y = 0;     // [-15:15]
middle_y = 0;    // [-15:15]
ring_y = 0;      // [-15:15]
pinky_y = 0;     // [-15:15]
pinky_far_y = 0; // [-15:15]
pinky_farer_y = 0; // [-15:15]

column_y_offsets =
    n_columns <= 4
        ? [index_y, ring_y, pinky_y, pinky_far_y]
        : n_columns == 5
            ? [index_far_y, index_y, ring_y, pinky_y, pinky_far_y]
            : n_columns == 6
                ? [index_far_y, index_y, middle_y, ring_y, pinky_y, pinky_far_y]
                : [index_far_y, index_y, middle_y, ring_y, pinky_y, pinky_far_y, pinky_farer_y];

active_column_y_offsets = column_y_offsets ;
if (offset_preset == "corne")  {
    active_column_y_offsets = [-12, -12, -6, 0, -6, -12];
    n_columns = 6;
}

module switch_hole() {
    cuboid([switch_hole_x, switch_hole_y, plate_thickness + epsilon], anchor=CENTER);
}

module single_key_plate() {
    difference() {
        cuboid([u, u, plate_thickness], anchor=CENTER);
        switch_hole();
    }
}

module vertical_stack_plate(n=4) {
    stack_h = n * u;

    difference() {
        cuboid([u, stack_h, plate_thickness], anchor=CENTER);

        for (i = [0 : n - 1]) {
            y = (i - (n - 1) / 2) * u;
            move([0, y, 0]) switch_hole();
        }
    }
}

module ortho_columns(
    n=4,
    columns=n_columns,
    column_y_offsets=column_y_offsets
) {
    for (i = [0 : columns - 1]) {
        x = (1 - i) * u;
        y = i < len(column_y_offsets) ? column_y_offsets[i] : 0;
        move([x, y, 0]) vertical_stack_plate(n=n);
    }
}

ortho_columns(columns=n_columns, column_y_offsets=active_column_y_offsets);
