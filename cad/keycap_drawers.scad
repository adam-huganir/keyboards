/* [Key Profile] */

fancy_render = true;
$fn = fancy_render ? 50 : 10;

// Select the key spacing standard used to size each tray footprint.
key_profile = "choc"; // [mx, choc]

/* [3D Printing] */

// 3D printing settings and validation.
spiral_vase = true; // [true, false]
nozzle_width_mm = 0.4; // [0.2:0.05:1.0]

/* [Key Spacing] */

// Standard key spacing dimensions.
mx_key_spacing_mm = 19.05; // [18:0.05:20]
choc_key_spacing_x_mm = 18; // [16:0.05:20]
choc_key_spacing_y_mm = 17; // [16:0.05:20]

// Shared wall, floor, and fit dimensions.
wall_thickness_mm = 0.4; // [0.2:0.05:2.0]
floor_thickness_mm = 0.4; // [0.2:0.05:2.0]
default_clearance_mm = 0.3; // [0:0.05:1.0]

// Effective print dimensions. Spiral vase mode forces single-line walls and floor.
effective_wall_thickness_mm = spiral_vase ? nozzle_width_mm : wall_thickness_mm;
effective_floor_thickness_mm = spiral_vase ? nozzle_width_mm : floor_thickness_mm;

assert(nozzle_width_mm > 0, "nozzle_width_mm must be greater than 0");
assert(wall_thickness_mm > 0, "wall_thickness_mm must be greater than 0");
assert(floor_thickness_mm > 0, "floor_thickness_mm must be greater than 0");
assert(default_clearance_mm >= 0, "default_clearance_mm must be non-negative");
assert(
  !spiral_vase || wall_thickness_mm == nozzle_width_mm,
  "spiral_vase requires wall_thickness_mm to match nozzle_width_mm"
);
assert(
  !spiral_vase || floor_thickness_mm == nozzle_width_mm,
  "spiral_vase requires floor_thickness_mm to match nozzle_width_mm"
);

/* [Tray Geometry] */

// Tray-specific sizing controls.
max_keycap_height_mm = 17; // [8:0.5:30]
tray_lip_height_mm = 5; // [1:0.5:20]
tray_length_u = 1; // [1:1:8]
handle_depth_mm = 10; // [0:0.5:20]
handle_width_mm = 15; // [0:0.5:20]
// Tiny vertical corner rounding to smooth toolpaths without materially changing fit.
vertical_corner_radius_mm = 0.4; // [0:0.05:1.0]

/* [Container Layout] */

// Container layout sizing: trays span the full row width, with one tray per row.
tray_count_x = 3; // [1:1:12]
tray_count_y = 2; // [1:1:12]
tray_container_clearance_mm = 0.3; // [0:0.05:1.0]

/* [Drawer] */

// Drawer fit sizing around the tray container.
drawer_clearance_mm = 0.3; // [0:0.05:1.0]

/* [Debug] */

// Spread the drawer, container, and trays apart for inspection.
debug_exploded_view = false; // [true, false]
debug_explode_distance_mm = 20; // [0:1:100]

/* [Hidden] */

// Resolve the active spacing from the selected key profile.
key_spacing_x_mm = key_profile == "mx" ? mx_key_spacing_mm : choc_key_spacing_x_mm;
key_spacing_y_mm = key_profile == "mx" ? mx_key_spacing_mm : choc_key_spacing_y_mm;

// A tray is fixed to 1u in y, while row width in x and lip height in z remain parametric.
row_tray_width_u = tray_count_x;
tray_height_mm = tray_lip_height_mm;
stack_height_mm = max_keycap_height_mm + default_clearance_mm * 2;
handle_angle_deg = 60;

// Inner tray envelope sized around one row-wide tray footprint plus fit clearance.
tray_inner_x_mm = key_spacing_x_mm * row_tray_width_u + default_clearance_mm * 2;
tray_inner_y_mm = key_spacing_y_mm * tray_length_u + default_clearance_mm * 2;
tray_inner_z_mm = tray_height_mm;

// Outer tray shell dimensions.
tray_outer_x_mm = tray_inner_x_mm + effective_wall_thickness_mm * 2;
tray_outer_y_mm = tray_inner_y_mm + effective_wall_thickness_mm * 2;
tray_outer_z_mm = tray_inner_z_mm + effective_floor_thickness_mm;
tray_outer_corner_radius_mm = min(vertical_corner_radius_mm, min(tray_outer_x_mm, tray_outer_y_mm) / 2);
tray_inner_corner_radius_mm = max(0, tray_outer_corner_radius_mm - effective_wall_thickness_mm);

// Container inner cavity sized to receive one tray per row and the full key stack height.
tray_container_inner_x_mm = tray_outer_x_mm + tray_container_clearance_mm * 2;
tray_container_inner_y_mm = tray_outer_y_mm * tray_count_y + tray_container_clearance_mm * 2;
tray_container_inner_z_mm = stack_height_mm + effective_floor_thickness_mm + tray_container_clearance_mm;

// Outer container shell dimensions.
tray_container_outer_x_mm = tray_container_inner_x_mm + effective_wall_thickness_mm * 2;
tray_container_outer_y_mm = tray_container_inner_y_mm + effective_wall_thickness_mm * 2;
tray_container_outer_z_mm = tray_container_inner_z_mm + effective_floor_thickness_mm;
tray_container_outer_corner_radius_mm = min(vertical_corner_radius_mm, min(tray_container_outer_x_mm, tray_container_outer_y_mm) / 2);
tray_container_inner_corner_radius_mm = max(0, tray_container_outer_corner_radius_mm - effective_wall_thickness_mm);
handle_rise_mm = min(10, tray_container_outer_z_mm);
handle_run_mm = handle_rise_mm / tan(handle_angle_deg);
handle_projection_mm = max(handle_depth_mm, handle_run_mm);
handle_face_offset_mm = max(0, handle_projection_mm - handle_run_mm);
handle_corner_radius_mm = min(2, handle_rise_mm / 2, handle_projection_mm / 2);
handle_fillet_adjacent_mm = handle_corner_radius_mm / tan(handle_angle_deg);
handle_hypotenuse_mm = handle_rise_mm / sin(handle_angle_deg);

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

module tray_container_handle_body() {
  translate(
    [
      (tray_container_outer_x_mm - handle_width_mm) / 2,
      0,
      effective_floor_thickness_mm + handle_rise_mm,
    ]
  )
    rotate([90, 180, 90])
      linear_extrude(height=handle_width_mm)
        polygon(
          points=[
            [handle_face_offset_mm, 0],
            [handle_projection_mm, 0],
            [handle_projection_mm - handle_run_mm, handle_rise_mm],
            [0, handle_rise_mm],
          ]
        );
}

module tray_container_handle_side_fillet_cutter(side) {
  if (side < 0) {
    difference() {
      translate(
        [
          (tray_container_outer_x_mm - handle_width_mm) / 2 - handle_corner_radius_mm,
          -handle_corner_radius_mm,
          effective_floor_thickness_mm,
        ]
      )
        cube(
          [
            handle_corner_radius_mm,
            handle_corner_radius_mm,
            handle_rise_mm,
          ]
        );
      translate(
        [
          (tray_container_outer_x_mm - handle_width_mm) / 2 - handle_corner_radius_mm,
          -handle_corner_radius_mm,
          effective_floor_thickness_mm,
        ]
      )
        cylinder(h=handle_rise_mm, r=handle_corner_radius_mm);
    }
  } else {
    translate(
      [
        (tray_container_outer_x_mm + handle_width_mm) / 2 + handle_corner_radius_mm,
        -handle_corner_radius_mm,
        effective_floor_thickness_mm,
      ]
    )
      rotate([0, 0, 90])
        translate(
          [
            -(tray_container_outer_x_mm + handle_width_mm) / 2,
            handle_corner_radius_mm,
            -effective_floor_thickness_mm,
          ]
        )
          difference() {
            translate(
              [
                (tray_container_outer_x_mm + handle_width_mm) / 2,
                -handle_corner_radius_mm,
                effective_floor_thickness_mm,
              ]
            )
              cube(
                [
                  handle_corner_radius_mm,
                  handle_corner_radius_mm,
                  handle_rise_mm,
                ]
              );
            translate(
              [
                (tray_container_outer_x_mm + handle_width_mm) / 2,
                -handle_corner_radius_mm,
                effective_floor_thickness_mm,
              ]
            )
              cylinder(h=handle_rise_mm, r=handle_corner_radius_mm);
          }
  }
}

module tray_container_handle_hypotenuse_fillet_cutter(side) {
  angle = 90 - handle_angle_deg;
  if (side < 0) {
    translate(
      [
        (tray_container_outer_x_mm - handle_width_mm) / 2 - handle_corner_radius_mm,
        -handle_corner_radius_mm * 2 * tan(angle),
        effective_floor_thickness_mm,
      ]
    )
      rotate([-angle, 0, 180])
        translate(
          [
            -( (tray_container_outer_x_mm - handle_width_mm) / 2 + handle_corner_radius_mm),
            -handle_corner_radius_mm,
            -effective_floor_thickness_mm - (handle_corner_radius_mm * tan(angle)),
          ]
        )
          difference() {
            translate(
              [
                (tray_container_outer_x_mm - handle_width_mm) / 2 - handle_corner_radius_mm,
                -handle_corner_radius_mm,
                effective_floor_thickness_mm,
              ]
            )
              cube(
                [
                  handle_corner_radius_mm,
                  handle_corner_radius_mm,
                  handle_hypotenuse_mm,
                ]
              );
            translate(
              [
                (tray_container_outer_x_mm - handle_width_mm) / 2 - handle_corner_radius_mm,
                -handle_corner_radius_mm,
                effective_floor_thickness_mm,
              ]
            )
              cylinder(h=handle_hypotenuse_mm, r=handle_corner_radius_mm);
          }
  } else {
    translate([tray_container_outer_x_mm, 0, 0])
      mirror([1, 0, 0])
        tray_container_handle_hypotenuse_fillet_cutter(-1);
  }
}

// Build the front tray-container handle as an angled prism rising from the base.
module tray_container_handle() {
  difference() {
    union() {
      tray_container_handle_body();
      tray_container_handle_side_fillet_cutter(-1);
      tray_container_handle_side_fillet_cutter(1);
    }
    ;
    tray_container_handle_hypotenuse_fillet_cutter(-1);
    tray_container_handle_hypotenuse_fillet_cutter(1);
  }
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
    tray_container_handle();
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
  for (iy = [0:tray_count_y - 1]) {
    translate(
      [
        effective_wall_thickness_mm + tray_container_clearance_mm,
        effective_wall_thickness_mm + tray_container_clearance_mm + iy * tray_outer_y_mm,
        effective_floor_thickness_mm,
      ]
    )
      key_tray();
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

if (debug_exploded_view) {
  exploded_drawer_assembly();
} else {
  drawer_assembly();
}
