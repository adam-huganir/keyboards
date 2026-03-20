/* [Print Layout] */

// Preview the parts in the optimal orientation for 3D printing.
print_orientation = true; // [true, false]
// Additional spacing between key trays in print orientation to prevent brim collision.
print_tray_spacing_mm = 5; // [0:1:50]

// printer bed dimensions
printer = "p1s"; // [p1s, ender3v2]
bed_x_mm = printer == "p1s" ? 250 : 220;
bed_y_mm = printer == "p1s" ? 250 : 220;

/* [Key Profile] */

// Select the key spacing standard used to size each tray footprint.
key_profile = "mx"; // [mx, choc]

/* [3D Printing] */

// 3D printing settings and validation.
nozzle_width_mm = 0.4; // [0.2:0.05:1.0]

// Shared wall and floor dimensions.
wall_lines = 2; // [1:1:5]
floor_layers = 2; // [1:1:5]

// Effective print dimensions.
effective_wall_thickness_mm = wall_lines * nozzle_width_mm;
effective_floor_thickness_mm = floor_layers * nozzle_width_mm;

assert(nozzle_width_mm > 0, "nozzle_width_mm must be greater than 0");
assert(wall_lines > 0, "wall_lines must be greater than 0");
assert(floor_layers > 0, "floor_layers must be greater than 0");
assert(default_clearance_mm >= 0, "default_clearance_mm must be non-negative");

/* [Clearance] */

// General fit clearance applied to most nested parts.
default_clearance_mm = 0.4; // [0:0.05:1.0]
// Fit clearance around the tray container inside the drawer.
drawer_clearance_mm = 0.4; // [0:0.05:1.0]
// Fit clearance around individual trays inside the container.
tray_container_clearance_mm = 0.3; // [0:0.05:1.0]

/* [Key Trays] */

// Layout sizing: trays span the full row width/depth, with one tray per row.
tray_orientation = "width"; // [width, length]
tray_count = [3, 2]; // [1:1:12]

// Tray-specific sizing controls.
keycap_height_preset = "OEM"; // [Custom, SA, OEM, Cherry, XDA, DSA, G20]
custom_max_keycap_height_mm = 17; // [6:0.1:20]
max_keycap_height_mm =
  keycap_height_preset == "SA" ? 16.5
  : keycap_height_preset == "OEM" ? 11.9
  : keycap_height_preset == "Cherry" ? 9.4
  : keycap_height_preset == "XDA" ? 9.1
  : keycap_height_preset == "DSA" ? 7.6
  : keycap_height_preset == "G20" ? 7.6
  : custom_max_keycap_height_mm;
tray_lip_height_mm = 4; // [1:0.5:20]
pull_triangle_top_from_bottom_mm = 9.1; // [0:0.5:40]

/* [Advanced Geometry] */

// Tiny vertical corner rounding to smooth toolpaths without materially changing fit.
vertical_corner_radius_mm = 0.4; // [0:0.05:1.0]

/* [Key Tray Spacing] */

// Standard key spacing dimensions.
mx_key_spacing_mm = 19.05; // [18:0.05:20]
choc_key_spacing_x_mm = 18; // [16:0.05:20]
choc_key_spacing_y_mm = 17; // [16:0.05:20]
tray_length_u = 1; // [1:1:8]

/* [Hidden] */

pull_triangle_height_mm = (max_keycap_height_mm + pull_triangle_top_from_bottom_mm )/3; // [1:0.5:20]
pull_triangle_width_mm = 7; // [8:0.5:80]
pull_triangle_depth_mm = 8; // [1:0.5:20]
pull_side_sphere_radius_mm = 5; // [0.5:0.1:20]
pull_side_sphere_wall_offset_mm = 3.6; // [0:0.1:10]
pull_side_sphere_surface_from_handle_center_mm = 0.2; // [0:0.1:2]

// Spread the drawer, container, and trays apart for inspection.
debug_exploded_view = false; // [true, false]
debug_explode_distance_mm = print_tray_spacing_mm; // [0:1:100]

fancy_render = true;
$fn = fancy_render ? 50 : 10;

// Resolve the active spacing from the selected key profile.
key_spacing_x_mm = key_profile == "mx" ? mx_key_spacing_mm : choc_key_spacing_x_mm;
key_spacing_y_mm = key_profile == "mx" ? mx_key_spacing_mm : choc_key_spacing_y_mm;

// A tray is fixed to 1u in y, while row width in x and lip height in z remain parametric.
row_tray_width_u = tray_orientation == "width" ? tray_count[0] : tray_length_u;
row_tray_length_u = tray_orientation == "width" ? tray_length_u : tray_count[1];
tray_height_mm = tray_lip_height_mm;
stack_height_mm = max_keycap_height_mm + default_clearance_mm * 2;

// Inner tray envelope sized around one row-wide tray footprint plus fit clearance.
tray_inner_x_mm = key_spacing_x_mm * row_tray_width_u + default_clearance_mm * 2;
tray_inner_y_mm = key_spacing_y_mm * row_tray_length_u + default_clearance_mm * 2;
tray_inner_z_mm = tray_height_mm;

// Outer tray shell dimensions.
tray_outer_x_mm = tray_inner_x_mm + effective_wall_thickness_mm * 2;
tray_outer_y_mm = tray_inner_y_mm + effective_wall_thickness_mm * 2;
tray_outer_z_mm = tray_inner_z_mm + effective_floor_thickness_mm;
tray_outer_corner_radius_mm = min(vertical_corner_radius_mm, min(tray_outer_x_mm, tray_outer_y_mm) / 2);
tray_inner_corner_radius_mm = max(0, tray_outer_corner_radius_mm - effective_wall_thickness_mm);

// Container inner cavity sized to receive one tray per row and the full key stack height.
tray_container_inner_x_mm =
  tray_orientation == "width" ?
    tray_outer_x_mm + tray_container_clearance_mm * 2
  : tray_outer_x_mm * tray_count[0] + tray_container_clearance_mm * 2;
tray_container_inner_y_mm =
  tray_orientation == "width" ?
    tray_outer_y_mm * tray_count[1] + tray_container_clearance_mm * 2
  : tray_outer_y_mm + tray_container_clearance_mm * 2;
tray_container_inner_z_mm = stack_height_mm + effective_floor_thickness_mm + tray_container_clearance_mm;

// Outer container shell dimensions.
tray_container_outer_x_mm = tray_container_inner_x_mm + effective_wall_thickness_mm * 2;
tray_container_outer_y_mm = tray_container_inner_y_mm + effective_wall_thickness_mm * 2;
tray_container_outer_z_mm = tray_container_inner_z_mm + effective_floor_thickness_mm;
tray_container_outer_corner_radius_mm = min(vertical_corner_radius_mm, min(tray_container_outer_x_mm, tray_container_outer_y_mm) / 2);
tray_container_inner_corner_radius_mm = max(0, tray_container_outer_corner_radius_mm - effective_wall_thickness_mm);

// Drawer inner cavity sized to receive the tray container from the front.
drawer_inner_x_mm = tray_container_outer_x_mm + drawer_clearance_mm * 2;
drawer_inner_y_mm = tray_container_outer_y_mm + drawer_clearance_mm + effective_wall_thickness_mm;
drawer_inner_z_mm = tray_container_outer_z_mm + drawer_clearance_mm;

// Outer drawer shell dimensions.
drawer_outer_x_mm = drawer_inner_x_mm + effective_wall_thickness_mm * 2;
drawer_outer_y_mm = drawer_inner_y_mm + effective_wall_thickness_mm;
drawer_outer_z_mm = drawer_inner_z_mm + effective_floor_thickness_mm + effective_wall_thickness_mm;
drawer_outer_corner_radius_mm = min(vertical_corner_radius_mm, min(drawer_outer_x_mm, drawer_outer_y_mm) / 2);
drawer_inner_corner_radius_mm = max(0, drawer_outer_corner_radius_mm - effective_wall_thickness_mm);

// Build a rounded rectangular prism with tiny fillets on the vertical corners.
module rounded_rect_prism(size, radius) {
  linear_extrude(height=size[2])
    offset(r=radius)
      translate([radius, radius])
        square(
          [
            max(0.01, size[0] - radius * 2),
            max(0.01, size[1] - radius * 2),
          ]
        );
}

module tray_container_front_pull_triangle() {
  pull_width_mm = min(
    pull_triangle_width_mm,
    tray_container_outer_x_mm - effective_wall_thickness_mm * 2
  );
  pull_height_mm = min(pull_triangle_height_mm, tray_container_outer_z_mm - effective_floor_thickness_mm);
  pull_depth_mm = min(pull_triangle_depth_mm, tray_container_outer_y_mm);
  pull_x_mm = (tray_container_outer_x_mm - pull_width_mm) / 2;
  pull_top_z_mm = min(
    tray_container_outer_z_mm - 0.01,
    max(effective_floor_thickness_mm + 0.01, pull_triangle_top_from_bottom_mm)
  );
  pull_bottom_z_mm = max(effective_floor_thickness_mm, pull_top_z_mm - pull_height_mm);
  pull_center_x_mm = pull_x_mm + pull_width_mm / 2;
  pull_center_z_mm = pull_top_z_mm;
  pull_mid_z_mm = (pull_top_z_mm + pull_bottom_z_mm) / 2;
  pull_sphere_radius_mm = pull_side_sphere_radius_mm;
  pull_sphere_center_x_mm =
    pull_center_x_mm + pull_side_sphere_surface_from_handle_center_mm + pull_sphere_radius_mm;
  pull_sphere_center_x_mirror_mm =
    pull_center_x_mm - pull_side_sphere_surface_from_handle_center_mm - pull_sphere_radius_mm;
  pull_sphere_center_y_mm = -pull_side_sphere_wall_offset_mm / 2;
  pull_sphere_center_z_mm = pull_mid_z_mm;
  pull_flat_face_from_drawer_mm = min(
    pull_depth_mm,
    max(0, pull_side_sphere_wall_offset_mm)
  );
  debug_epsilon_mm = 0.01;
  pull_base_y_mm = debug_epsilon_mm;

  if (pull_width_mm > 0 && pull_height_mm > 0 && pull_depth_mm > 0)
    if (pull_sphere_radius_mm > 0)
      render(convexity=10)
        difference() {
          polyhedron(
            points = [
              [pull_x_mm, pull_base_y_mm, pull_top_z_mm],
              [pull_x_mm + pull_width_mm, pull_base_y_mm, pull_top_z_mm],
              [pull_center_x_mm, pull_base_y_mm, pull_bottom_z_mm],
              [pull_center_x_mm, -pull_depth_mm, pull_center_z_mm],
            ],
            faces = [
              [0, 1, 2],
              [0, 3, 1],
              [1, 3, 2],
              [2, 3, 0],
            ],
            convexity = 10
          );
          translate([pull_sphere_center_x_mm, pull_sphere_center_y_mm, pull_sphere_center_z_mm])
            sphere(r=pull_sphere_radius_mm);
          translate([pull_sphere_center_x_mirror_mm, pull_sphere_center_y_mm, pull_sphere_center_z_mm])
            sphere(r=pull_sphere_radius_mm);
          if (pull_flat_face_from_drawer_mm < pull_depth_mm)
            translate([pull_x_mm - debug_epsilon_mm, -pull_depth_mm - debug_epsilon_mm, pull_bottom_z_mm - debug_epsilon_mm])
              cube([
                pull_width_mm + debug_epsilon_mm * 2,
                pull_depth_mm - pull_flat_face_from_drawer_mm + debug_epsilon_mm,
                pull_top_z_mm - pull_bottom_z_mm + debug_epsilon_mm * 2,
              ]);
        }
    else
      render(convexity=10)
        polyhedron(
          points = [
            [pull_x_mm, pull_base_y_mm, pull_top_z_mm],
            [pull_x_mm + pull_width_mm, pull_base_y_mm, pull_top_z_mm],
            [pull_center_x_mm, pull_base_y_mm, pull_bottom_z_mm],
            [pull_center_x_mm, -pull_depth_mm, pull_center_z_mm],
          ],
          faces = [
            [0, 1, 2],
            [0, 3, 1],
            [1, 3, 2],
            [2, 3, 0],
          ],
          convexity = 10
        );
}

// Build a single open-top tray.
module key_tray() {
  difference() {
    rounded_rect_prism(
      [tray_outer_x_mm, tray_outer_y_mm, tray_outer_z_mm],
      tray_outer_corner_radius_mm
    );
    translate([effective_wall_thickness_mm, effective_wall_thickness_mm, effective_floor_thickness_mm])
      rounded_rect_prism(
        [tray_inner_x_mm, tray_inner_y_mm, tray_inner_z_mm],
        tray_inner_corner_radius_mm
      );
  }
}

// Build the open-top container shell that holds one or more trays.
module tray_container() {
  union() {
    difference() {
      rounded_rect_prism(
        [tray_container_outer_x_mm, tray_container_outer_y_mm, tray_container_outer_z_mm],
        tray_container_outer_corner_radius_mm
      );
      translate([effective_wall_thickness_mm, effective_wall_thickness_mm, effective_floor_thickness_mm])
        rounded_rect_prism(
          [tray_container_inner_x_mm, tray_container_inner_y_mm, tray_container_inner_z_mm],
          tray_container_inner_corner_radius_mm
        );
    }
    tray_container_front_pull_triangle();
  }
}

// Build the outer drawer shell with a front opening for the tray container.
module outer_drawer() {
  difference() {
    rounded_rect_prism(
      [drawer_outer_x_mm, drawer_outer_y_mm, drawer_outer_z_mm],
      drawer_outer_corner_radius_mm
    );
    translate([effective_wall_thickness_mm, 0, effective_floor_thickness_mm])
      rounded_rect_prism(
        [drawer_inner_x_mm, drawer_inner_y_mm, drawer_inner_z_mm],
        drawer_inner_corner_radius_mm
      );
  }
}

// Place one tray in each row so the tray width follows the container width.
module tray_container_layout() {
  if (tray_orientation == "width") {
    for (iy = [0:tray_count[1] - 1]) {
      translate(
        [
          effective_wall_thickness_mm + tray_container_clearance_mm,
          effective_wall_thickness_mm + tray_container_clearance_mm + iy * tray_outer_y_mm,
          effective_floor_thickness_mm,
        ]
      )
        key_tray();
    }
  } else {
    for (ix = [0:tray_count[0] - 1]) {
      translate(
        [
          effective_wall_thickness_mm + tray_container_clearance_mm + ix * tray_outer_x_mm,
          effective_wall_thickness_mm + tray_container_clearance_mm,
          effective_floor_thickness_mm,
        ]
      )
        key_tray();
    }
  }
}

// Preview the fitted relationship between the tray container and its trays.
module tray_container_assembly() {
  tray_container();
  tray_container_layout();
}

// Preview the drawer, container, and trays separated for easier inspection.
module exploded_drawer_assembly() {
  outer_drawer();
  translate(
    [
      drawer_outer_x_mm + debug_explode_distance_mm,
      0,
      0,
    ]
  )
    tray_container();
  translate(
    [
      drawer_outer_x_mm + tray_container_outer_x_mm + debug_explode_distance_mm * 2,
      0,
      0,
    ]
  )
    tray_container_layout();
}

// Preview the fitted relationship between the drawer, container, and trays.
module drawer_assembly() {
  outer_drawer();
  translate(
    [
      effective_wall_thickness_mm + drawer_clearance_mm,
      0,
      effective_floor_thickness_mm,
    ]
  )
    tray_container_assembly();
}

module print_drawer_assembly() {
  num_trays = tray_orientation == "width" ? tray_count[1] : tray_count[0];

  // 1. Drawer goes first, bottom-left
  // It is rotated so it stands on its back.
  drawer_print_x = drawer_outer_x_mm;
  drawer_print_y = drawer_outer_z_mm; // Z becomes Y after rotation

  translate([0, 0, drawer_outer_y_mm])
    rotate([-90, 0, 0])
      outer_drawer();

  // 2. Container
  // If it fits next to the drawer, put it there, otherwise stack above
  container_fits_x = (drawer_print_x + print_tray_spacing_mm + tray_container_outer_x_mm) <= bed_x_mm;
  container_x = container_fits_x ? drawer_print_x + print_tray_spacing_mm : 0;
  container_y = container_fits_x ? 0 : drawer_print_y + print_tray_spacing_mm;

  translate([container_x, container_y, 0])
    tray_container();

  // 3. Trays (arranged in a grid)
  trays_start_y = max(
    drawer_print_y,
    container_y + tray_container_outer_y_mm
  ) + print_tray_spacing_mm;

  trays_per_row = max(1, floor((bed_x_mm + print_tray_spacing_mm) / (tray_outer_x_mm + print_tray_spacing_mm)));

  for (i = [0:num_trays - 1]) {
    col = i % trays_per_row;
    row = floor(i / trays_per_row);
    translate(
      [
        col * (tray_outer_x_mm + print_tray_spacing_mm),
        trays_start_y + row * (tray_outer_y_mm + print_tray_spacing_mm),
        0,
      ]
    )
      key_tray();
  }
}

if (print_orientation) {
  print_drawer_assembly();
} else if (debug_exploded_view) {
  exploded_drawer_assembly();
} else {
  drawer_assembly();
}
