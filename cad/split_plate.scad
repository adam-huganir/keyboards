include <BOSL2/std.scad>

/* [Units] */
key = "mx"; // [mx, choc]
u = key == "mx" ? 19.05 : 18.0; // Standard key spacing (1u)

/* [Layout] */
n_columns = 6; // [4 : 7]
n_rows = 4; // [1 : 6]
offset_preset = "custom"; // [custom, corne]

index_far_y = 0; // [-15:15]
index_y = 0; // [-15:15]
middle_y = 0; // [-15:15]
ring_y = 0; // [-15:15]
pinky_y = 0; // [-15:15]
pinky_far_y = 0; // [-15:15]
pinky_farer_y = 0; // [-15:15]

/* [Rendering] */
render_side = "left"; // [left, right, both]
hull_mode = "none"; // [none, convex, chain]
column_outer_padding_mm = 0; // [0:0.1:5]

/* [Thumb Cluster] */
thumb_preset = "custom"; // [custom, corne]
thumb_rows = 1; // [1:1]
thumb_keys = 3; // [1:5]
thumb_offset_x_mm = -8; // [-50:1:50]
thumb_offset_y_mm = -48; // [-100:1:100]
thumb_corne_x_adjust_mm = 0; // [-20:1:20]
thumb_corne_y_adjust_mm = 0; // [-20:1:20]
thumb_corne_splay_step_deg = 11.94; // [0:0.01:30]

/* [Derived Layout] */

column_y_offsets =
  n_columns <= 4 ? [index_y, ring_y, pinky_y, pinky_far_y]
  : n_columns == 5 ? [index_far_y, index_y, ring_y, pinky_y, pinky_far_y]
  : n_columns == 6 ? [index_far_y, index_y, middle_y, ring_y, pinky_y, pinky_far_y]
  : [index_far_y, index_y, middle_y, ring_y, pinky_y, pinky_far_y, pinky_farer_y];

active_n_columns = offset_preset == "corne" ? 6 : n_columns;
active_n_rows = offset_preset == "corne" ? 3 : n_rows;
active_column_y_offsets =
  offset_preset == "corne" ? [-12, -6, 0, -6, -12, -12]
  : column_y_offsets;
index_column_i = 0;
active_index_column_x = (1 - index_column_i) * u;
active_index_column_y = active_column_y_offsets[index_column_i];

corne_extra_index_keys = offset_preset == "corne" ? 2 : 0;
corne_extra_index_x = active_index_column_x + u;
corne_inner_middle_row_y = active_column_y_offsets[0];
corne_extra_index_top_y = corne_inner_middle_row_y + u / 2;

// Corne thumb preset geometry.
corne_index_column_i = active_n_columns > 1 ? 1 : 0;
corne_middle_column_i = active_n_columns > 2 ? 2 : corne_index_column_i;
corne_left_key_center_x =
( (1 - corne_index_column_i) * u + (1 - corne_middle_column_i) * u) / 2 + thumb_corne_x_adjust_mm;
corne_index_far_bottom_y = active_column_y_offsets[0] - active_n_rows * u / 2;
corne_left_key_center_y = corne_index_far_bottom_y - u / 2 + thumb_corne_y_adjust_mm;

// Corne thumb preset overrides.
active_thumb_rows = thumb_preset == "corne" ? 1 : thumb_rows;
active_thumb_keys = thumb_preset == "corne" ? 3 : thumb_keys;

thumb_anchor_x =
  thumb_preset == "corne" ? corne_left_key_center_x + (active_thumb_keys - 1) / 2 * u
  : active_index_column_x + thumb_offset_x_mm;
thumb_anchor_y =
  thumb_preset == "corne" ? corne_left_key_center_y
  : active_index_column_y + thumb_offset_y_mm;

/* [Advanced Constants] */

plate_thickness = 3.0; // [1.0:0.2:4.0]
epsilon = 0.01;

switch_hole_width = 14.0; // MX switch cutout width
switch_hole_height = 14.0; // MX switch cutout height
plate_switch_clearance = 0.05; // Extra clearance per side

switch_hole_x = switch_hole_width + 2 * plate_switch_clearance;
switch_hole_y = switch_hole_height + 2 * plate_switch_clearance;

module switch_hole() {
  cuboid([switch_hole_x, switch_hole_y, plate_thickness + epsilon], anchor=CENTER);
}

module single_key_plate() {
  difference() {
    cuboid([u, u, plate_thickness], anchor=CENTER);
    switch_hole();
  }
}

module corne_extra_index_column_padded(
  keys = corne_extra_index_keys,
  padding = 0
) {
  if (keys > 0) {
    for (k = [0:keys - 1]) {
      y = corne_extra_index_top_y - k * u;
      move([corne_extra_index_x, y, 0]) vertical_stack_plate_padded(n=1, padding=padding);
    }
  }
}

module corne_extra_index_column_solid_padded(
  keys = corne_extra_index_keys,
  padding = 0
) {
  if (keys > 0) {
    for (k = [0:keys - 1]) {
      y = corne_extra_index_top_y - k * u;
      move([corne_extra_index_x, y, 0]) vertical_stack_plate_solid_padded(n=1, padding=padding);
    }
  }
}

module corne_extra_index_column_switch_holes(keys = corne_extra_index_keys) {
  if (keys > 0) {
    for (k = [0:keys - 1]) {
      y = corne_extra_index_top_y - k * u;
      move([corne_extra_index_x, y, 0]) column_switch_holes(n=1);
    }
  }
}

module vertical_stack_plate_padded(n = 4, padding = 0) {
  stack_h = n * u;
  pad = max(0, padding);

  difference() {
    cuboid([u + 2 * pad, stack_h + 2 * pad, plate_thickness], anchor=CENTER);

    for (i = [0:n - 1]) {
      y = (i - (n - 1) / 2) * u;
      move([0, y, 0]) switch_hole();
    }
  }
}

module vertical_stack_plate_solid(n = 4) {
  stack_h = n * u;
  cuboid([u, stack_h, plate_thickness], anchor=CENTER);
}

module vertical_stack_plate_solid_padded(n = 4, padding = 0) {
  stack_h = n * u;
  pad = max(0, padding);
  cuboid([u + 2 * pad, stack_h + 2 * pad, plate_thickness], anchor=CENTER);
}

module column_switch_holes(n = 4) {
  for (i = [0:n - 1]) {
    y = (i - (n - 1) / 2) * u;
    move([0, y, 0]) switch_hole();
  }
}

module vertical_stack_plate(n = 4) {
  stack_h = n * u;

  difference() {
    cuboid([u, stack_h, plate_thickness], anchor=CENTER);

    for (i = [0:n - 1]) {
      y = (i - (n - 1) / 2) * u;
      move([0, y, 0]) switch_hole();
    }
  }
}

module ortho_columns(
  n = 4,
  columns = n_columns,
  column_y_offsets = column_y_offsets
) {
  for (i = [0:columns - 1]) {
    x = (1 - i) * u;
    y = i < len(column_y_offsets) ? column_y_offsets[i] : 0;
    move([x, y, 0]) vertical_stack_plate(n=n);
  }
}

module ortho_columns_padded(
  n = 4,
  columns = n_columns,
  column_y_offsets = column_y_offsets,
  padding = 0
) {
  for (i = [0:columns - 1]) {
    x = (1 - i) * u;
    y = i < len(column_y_offsets) ? column_y_offsets[i] : 0;
    move([x, y, 0]) vertical_stack_plate_padded(n=n, padding=padding);
  }
}

module ortho_columns_solid(
  n = 4,
  columns = n_columns,
  column_y_offsets = column_y_offsets
) {
  for (i = [0:columns - 1]) {
    x = (1 - i) * u;
    y = i < len(column_y_offsets) ? column_y_offsets[i] : 0;
    move([x, y, 0]) vertical_stack_plate_solid(n=n);
  }
}

module ortho_columns_solid_padded(
  n = 4,
  columns = n_columns,
  column_y_offsets = column_y_offsets,
  padding = 0
) {
  for (i = [0:columns - 1]) {
    x = (1 - i) * u;
    y = i < len(column_y_offsets) ? column_y_offsets[i] : 0;
    move([x, y, 0]) vertical_stack_plate_solid_padded(n=n, padding=padding);
  }
}

module ortho_column_switch_holes(
  n = 4,
  columns = n_columns,
  column_y_offsets = column_y_offsets
) {
  for (i = [0:columns - 1]) {
    x = (1 - i) * u;
    y = i < len(column_y_offsets) ? column_y_offsets[i] : 0;
    move([x, y, 0]) column_switch_holes(n=n);
  }
}

function rotate2d(v, deg) =
  [
    v[0] * cos(deg) - v[1] * sin(deg),
    v[0] * sin(deg) + v[1] * cos(deg),
  ];

function thumb_key_angle_deg(k) = thumb_preset == "corne" ? -k * thumb_corne_splay_step_deg : 0;

function thumb_key_length_u(k, keys) = thumb_preset == "corne" && k == keys - 1 ? 1.5 : 1;

function thumb_key_body_center_shift_y(k, keys) = (thumb_key_length_u(k, keys) - 1) * u / 2;

function thumb_key_center_from_left(k, left_center_xy) =
  k == 0 ? left_center_xy
  : let (
    prev_center = thumb_key_center_from_left(k - 1, left_center_xy),
    prev_angle = thumb_key_angle_deg(k - 1),
    prev_bottom_right = prev_center + rotate2d([u / 2, -u / 2], prev_angle),
    curr_angle = thumb_key_angle_deg(k),
    curr_center_offset = rotate2d([u / 2, u / 2], curr_angle)
  ) prev_bottom_right + curr_center_offset;

module thumb_single_key_padded(
  length_u = 1,
  padding = 0
) {
  key_l = u * length_u;
  pad = max(0, padding);

  difference() {
    cuboid([u + 2 * pad, key_l + 2 * pad, plate_thickness], anchor=CENTER);
    switch_hole();
  }
}

module thumb_single_key_solid_padded(
  length_u = 1,
  padding = 0
) {
  key_l = u * length_u;
  pad = max(0, padding);
  cuboid([u + 2 * pad, key_l + 2 * pad, plate_thickness], anchor=CENTER);
}

module thumb_cluster_padded(
  rows = active_thumb_rows,
  keys = active_thumb_keys,
  padding = 0
) {
  for (r = [0:rows - 1]) {
    row_left_center = [thumb_anchor_x - (keys - 1) / 2 * u, thumb_anchor_y - r * u];
    for (k = [0:keys - 1]) {
      hole_center_xy = thumb_key_center_from_left(k, row_left_center);
      rot_deg = thumb_key_angle_deg(k);
      body_shift_y = thumb_key_body_center_shift_y(k, keys);
      body_center_xy = hole_center_xy + rotate2d([0, body_shift_y], rot_deg);
      move([body_center_xy[0], body_center_xy[1], 0])
        rotate([0, 0, rot_deg])
          thumb_single_key_padded(
            length_u=thumb_key_length_u(k, keys),
            padding=padding
          );
    }
  }
}

module thumb_cluster_solid_padded(
  rows = active_thumb_rows,
  keys = active_thumb_keys,
  padding = 0
) {
  for (r = [0:rows - 1]) {
    row_left_center = [thumb_anchor_x - (keys - 1) / 2 * u, thumb_anchor_y - r * u];
    for (k = [0:keys - 1]) {
      hole_center_xy = thumb_key_center_from_left(k, row_left_center);
      rot_deg = thumb_key_angle_deg(k);
      body_shift_y = thumb_key_body_center_shift_y(k, keys);
      body_center_xy = hole_center_xy + rotate2d([0, body_shift_y], rot_deg);
      move([body_center_xy[0], body_center_xy[1], 0])
        rotate([0, 0, rot_deg])
          thumb_single_key_solid_padded(
            length_u=thumb_key_length_u(k, keys),
            padding=padding
          );
    }
  }
}

module thumb_cluster_switch_holes(
  rows = active_thumb_rows,
  keys = active_thumb_keys
) {
  for (r = [0:rows - 1]) {
    row_left_center = [thumb_anchor_x - (keys - 1) / 2 * u, thumb_anchor_y - r * u];
    for (k = [0:keys - 1]) {
      center_xy = thumb_key_center_from_left(k, row_left_center);
      rot_deg = thumb_key_angle_deg(k);
      move([center_xy[0], center_xy[1], 0]) rotate([0, 0, rot_deg]) column_switch_holes(n=1);
    }
  }
}

module split_plate_half() {
  ortho_columns_padded(
    n=active_n_rows,
    columns=active_n_columns,
    column_y_offsets=active_column_y_offsets,
    padding=column_outer_padding_mm
  );
  corne_extra_index_column_padded(padding=column_outer_padding_mm);
  thumb_cluster_padded(padding=column_outer_padding_mm);
}

module split_plate_half_hull_body() {
  if (hull_mode == "convex") {
    hull() {
      ortho_columns_solid_padded(
        n=active_n_rows,
        columns=active_n_columns,
        column_y_offsets=active_column_y_offsets,
        padding=column_outer_padding_mm
      );
      corne_extra_index_column_solid_padded(padding=column_outer_padding_mm);
      thumb_cluster_solid_padded(padding=column_outer_padding_mm);
    }
  } else {
    chain_hull() {
      ortho_columns_solid_padded(
        n=active_n_rows,
        columns=active_n_columns,
        column_y_offsets=active_column_y_offsets,
        padding=column_outer_padding_mm
      );
      corne_extra_index_column_solid_padded(padding=column_outer_padding_mm);
      thumb_cluster_solid_padded(padding=column_outer_padding_mm);
    }
  }
}

module split_plate_half_hulled_with_cutouts() {
  difference() {
    split_plate_half_hull_body();
    ortho_column_switch_holes(n=active_n_rows, columns=active_n_columns, column_y_offsets=active_column_y_offsets);
    corne_extra_index_column_switch_holes();
    thumb_cluster_switch_holes();
  }
}

translate([0, u, 0]) {
  if (render_side == "left") {
    if (hull_mode != "none") {
      split_plate_half_hulled_with_cutouts();
    } else {
      split_plate_half();
    }
  } else if (render_side == "right") {
    if (hull_mode != "none") {
      mirror([1, 0, 0]) split_plate_half_hulled_with_cutouts();
    } else {
      mirror([1, 0, 0]) split_plate_half();
    }
  } else {
    if (hull_mode != "none") {
      translate([7 * u, 0, 0]) split_plate_half_hulled_with_cutouts();
      mirror([1, 0, 0]) translate([7 * u, 0, 0]) split_plate_half_hulled_with_cutouts();
    } else {
      translate([7 * u, 0, 0]) split_plate_half();
      mirror([1, 0, 0]) translate([7 * u, 0, 0]) split_plate_half();
    }
  }
}
