{
  'targets': [
    {
      'target_name': 'system_api-protos-gen',
      'type': 'none',
      'variables': {
        'proto_in_dir': 'dbus',
        'proto_out_dir': 'include/system_api/proto_bindings',
      },
      'sources': [
        '<(proto_in_dir)/mtp_storage_info.proto',
        '<(proto_in_dir)/mtp_file_entry.proto',
        '<(proto_in_dir)/field_trial_list.proto',
      ],
      'includes': ['../../platform2/common-mk/protoc.gypi'],
    },
    {
      'target_name': 'system_api-protos',
      'type': 'static_library',
      'standalone_static_library': 1,
      'dependencies': [
        'system_api-protos-gen',
      ],
      'sources': [
        '<(SHARED_INTERMEDIATE_DIR)/include/system_api/proto_bindings/mtp_storage_info.pb.cc',
        '<(SHARED_INTERMEDIATE_DIR)/include/system_api/proto_bindings/mtp_file_entry.pb.cc',
        '<(SHARED_INTERMEDIATE_DIR)/include/system_api/proto_bindings/field_trial_list.pb.cc',
      ]
    },
    {
      'target_name': 'system_api-power_manager-protos-gen',
      'type': 'none',
      'variables': {
        'proto_in_dir': 'dbus/power_manager',
        'proto_out_dir': 'include/power_manager/proto_bindings',
      },
      'sources': [
        '<(proto_in_dir)/backlight.proto',
        '<(proto_in_dir)/idle.proto',
        '<(proto_in_dir)/input_event.proto',
        '<(proto_in_dir)/peripheral_battery_status.proto',
        '<(proto_in_dir)/policy.proto',
        '<(proto_in_dir)/power_supply_properties.proto',
        '<(proto_in_dir)/suspend.proto',
        '<(proto_in_dir)/switch_states.proto',
      ],
      'includes': ['../../platform2/common-mk/protoc.gypi'],
    },
    {
      'target_name': 'system_api-power_manager-protos',
      'type': 'static_library',
      'standalone_static_library': 1,
      'dependencies': [
        'system_api-power_manager-protos-gen',
      ],
      'sources': [
        '<(SHARED_INTERMEDIATE_DIR)/include/power_manager/proto_bindings/backlight.pb.cc',
        '<(SHARED_INTERMEDIATE_DIR)/include/power_manager/proto_bindings/idle.pb.cc',
        '<(SHARED_INTERMEDIATE_DIR)/include/power_manager/proto_bindings/input_event.pb.cc',
        '<(SHARED_INTERMEDIATE_DIR)/include/power_manager/proto_bindings/peripheral_battery_status.pb.cc',
        '<(SHARED_INTERMEDIATE_DIR)/include/power_manager/proto_bindings/policy.pb.cc',
        '<(SHARED_INTERMEDIATE_DIR)/include/power_manager/proto_bindings/power_supply_properties.pb.cc',
        '<(SHARED_INTERMEDIATE_DIR)/include/power_manager/proto_bindings/suspend.pb.cc',
        '<(SHARED_INTERMEDIATE_DIR)/include/power_manager/proto_bindings/switch_states.pb.cc',
      ]
    },
    {
      'target_name': 'system_api-cryptohome-protos-gen',
      'type': 'none',
      'variables': {
        'proto_in_dir': 'dbus/cryptohome',
        'proto_out_dir': 'include/cryptohome/proto_bindings',
      },
      'sources': [
        '<(proto_in_dir)/key.proto',
        '<(proto_in_dir)/rpc.proto',
        '<(proto_in_dir)/signed_secret.proto',
      ],
      'includes': ['../../platform2/common-mk/protoc.gypi'],
    },
    {
      'target_name': 'system_api-cryptohome-protos',
      'type': 'static_library',
      'standalone_static_library': 1,
      'dependencies': [
        'system_api-cryptohome-protos-gen',
      ],
      'sources': [
        '<(SHARED_INTERMEDIATE_DIR)/include/cryptohome/proto_bindings/key.pb.cc',
        '<(SHARED_INTERMEDIATE_DIR)/include/cryptohome/proto_bindings/rpc.pb.cc',
        '<(SHARED_INTERMEDIATE_DIR)/include/cryptohome/proto_bindings/signed_secret.pb.cc',
      ]
    },
    {
      'target_name': 'system_api-authpolicy-protos-gen',
      'type': 'none',
      'variables': {
        'proto_in_dir': 'dbus/authpolicy',
        'proto_out_dir': 'include/authpolicy/proto_bindings',
      },
      'sources': [
        '<(proto_in_dir)/active_directory_info.proto',
      ],
      'includes': ['../../platform2/common-mk/protoc.gypi'],
    },
    {
      'target_name': 'system_api-authpolicy-protos',
      'type': 'static_library',
      'standalone_static_library': 1,
      'dependencies': [
        'system_api-authpolicy-protos-gen',
      ],
      'sources': [
        '<(SHARED_INTERMEDIATE_DIR)/include/authpolicy/proto_bindings/active_directory_info.pb.cc',
      ]
    },
    {
      'target_name': 'system_api-biod-protos-gen',
      'type': 'none',
      'variables': {
        'proto_in_dir': 'dbus/biod',
        'proto_out_dir': 'include/biod/proto_bindings',
      },
      'sources': [
        '<(proto_in_dir)/constants.proto',
        '<(proto_in_dir)/messages.proto',
      ],
      'includes': ['../../platform2/common-mk/protoc.gypi'],
    },
    {
      'target_name': 'system_api-biod-protos',
      'type': 'static_library',
      'standalone_static_library': 1,
      'dependencies': [
        'system_api-biod-protos-gen',
      ],
      'sources': [
        '<(SHARED_INTERMEDIATE_DIR)/include/biod/proto_bindings/constants.pb.cc',
        '<(SHARED_INTERMEDIATE_DIR)/include/biod/proto_bindings/messages.pb.cc',
      ]
    },
    {
      'target_name': 'system_api-login_manager-protos-gen',
      'type': 'none',
      'variables': {
        'proto_in_dir': 'dbus/login_manager',
        'proto_out_dir': 'include/login_manager/proto_bindings',
      },
      'sources': [
        '<(proto_in_dir)/arc.proto',
        '<(proto_in_dir)/policy_descriptor.proto',
      ],
      'includes': ['../../platform2/common-mk/protoc.gypi'],
    },
    {
      'target_name': 'system_api-login_manager-protos',
      'type': 'static_library',
      'standalone_static_library': 1,
      'dependencies': [
        'system_api-login_manager-protos-gen',
      ],
      'sources': [
        '<(SHARED_INTERMEDIATE_DIR)/include/login_manager/proto_bindings/arc.pb.cc',
        '<(SHARED_INTERMEDIATE_DIR)/include/login_manager/proto_bindings/policy_descriptor.pb.cc',
      ]
    },
    {
      'target_name': 'system_api-chaps-protos-gen',
      'type': 'none',
      'variables': {
        'proto_in_dir': 'dbus/chaps',
        'proto_out_dir': 'include/chaps/proto_bindings',
      },
      'sources': [
        '<(proto_in_dir)/ck_structs.proto',
      ],
      'includes': ['../../platform2/common-mk/protoc.gypi'],
    },
    {
      'target_name': 'system_api-chaps-protos',
      'type': 'static_library',
      # system_api-chaps-protos' is used by a shared_library
      # object, so we need to build it with '-fPIC' instead of '-fPIE'.
      'cflags!': ['-fPIE'],
      'cflags': ['-fPIC'],
      'standalone_static_library': 1,
      'dependencies': [
        'system_api-chaps-protos-gen',
      ],
      'sources': [
        '<(SHARED_INTERMEDIATE_DIR)/include/chaps/proto_bindings/ck_structs.pb.cc',
      ]
    },
    {
      'target_name': 'system_api-smbprovider-protos-gen',
      'type': 'none',
      'variables': {
        'proto_in_dir': 'dbus/smbprovider',
        'proto_out_dir': 'include/smbprovider/proto_bindings',
      },
      'sources': [
        '<(proto_in_dir)/directory_entry.proto',
      ],
      'includes': ['../../platform2/common-mk/protoc.gypi'],
    },
    {
      'target_name': 'system_api-smbprovider-protos',
      'type': 'static_library',
      'standalone_static_library': 1,
      'dependencies': [
        'system_api-smbprovider-protos-gen',
      ],
      'sources': [
        '<(SHARED_INTERMEDIATE_DIR)/include/smbprovider/proto_bindings/directory_entry.pb.cc',
      ]
    },
    {
      'target_name': 'system_api-vm_concierge-protos-gen',
      'type': 'none',
      'variables': {
        'proto_in_dir': 'dbus/vm_concierge',
        'proto_out_dir': 'include/vm_concierge/proto_bindings',
      },
      'sources': [
        '<(proto_in_dir)/service.proto',
      ],
      'includes': ['../../platform2/common-mk/protoc.gypi'],
    },
    {
      'target_name': 'system_api-vm_concierge-goprotos-gen',
      'type': 'none',
      'variables': {
        'gen_go': 1,
        'proto_in_dir': 'dbus/vm_concierge',
        'proto_out_dir': 'go/src/chromiumos/system_api/vm_concierge',
      },
      'sources': [
        '<(proto_in_dir)/service.proto',
      ],
      'includes': ['../../platform2/common-mk/protoc.gypi'],
    },
    {
      'target_name': 'system_api-vm_concierge-protos',
      'type': 'static_library',
      'standalone_static_library': 1,
      'dependencies': [
        'system_api-vm_concierge-protos-gen',
      ],
      'sources': [
        '<(SHARED_INTERMEDIATE_DIR)/include/vm_concierge/proto_bindings/service.pb.cc',
      ]
    },
    {
      'target_name': 'system_api-vm_applications-protos-gen',
      'type': 'none',
      'variables': {
        'proto_in_dir': 'dbus/vm_applications',
        'proto_out_dir': 'include/vm_applications/proto_bindings',
      },
      'sources': [
        '<(proto_in_dir)/apps.proto',
      ],
      'includes': ['../../platform2/common-mk/protoc.gypi'],
    },
    {
      'target_name': 'system_api-vm_applications-protos',
      'type': 'static_library',
      'standalone_static_library': 1,
      'dependencies': [
        'system_api-vm_applications-protos-gen',
      ],
      'sources': [
        '<(SHARED_INTERMEDIATE_DIR)/include/vm_applications/proto_bindings/apps.pb.cc',
      ]
    },
    {
      'target_name': 'ml_service_mojo_bindings',
      'type': 'static_library',
      'variables': {
        'deps': [
          'libchrome-<(libbase_ver)',
          'libmojo-<(libbase_ver)',
        ],
        'mojo_output_dir': '<(SHARED_INTERMEDIATE_DIR)/include',
        'mojo_binding_generator': '<(sysroot)/usr/src/libmojo-<(libbase_ver)/mojo/mojom_bindings_generator.py',
        'mojo_template_dir': '<(SHARED_INTERMEDIATE_DIR)/templates',
      },
      'sources': [
        'mojo/ml_service/interface.mojom',
        'mojo/ml_service/learning_example.mojom',
        'mojo/ml_service/model.mojom',
      ],
      'actions': [
        {
          'action_name': 'ml_service_mojom_templates_dir',
          'inputs': [
          ],
          'outputs': [
            '<(mojo_template_dir)',
          ],
          'message': 'Creating mojo C++ templates dir <(mojo_template_dir)',
          'action': [
            'mkdir', '-p', '<(mojo_template_dir)',
          ],
        },
        {
          'action_name': 'ml_service_mojom_templates',
          'inputs': [
            '<(mojo_binding_generator)',
            '<(mojo_template_dir)',
          ],
          'outputs': [
            '<(mojo_template_dir)/cpp_templates.zip',
          ],
          'message': 'Generating mojo C++ templates in <(mojo_template_dir)',
          'action': [
            'python', '<(mojo_binding_generator)', '--use_bundled_pylibs',
            'precompile', '-o', '<(mojo_template_dir)',
          ],
        },
      ],
      'rules': [
        {
          'rule_name': 'ml_service_mojom_bindings_gen',
          'extension': 'mojom',
          'inputs': [
            '<(mojo_binding_generator)',
            '<(mojo_template_dir)/cpp_templates.zip',
          ],
          'outputs': [
            '<(mojo_output_dir)/mojo/ml_service/<(RULE_INPUT_NAME)-internal.h',
            '<(mojo_output_dir)/mojo/ml_service/<(RULE_INPUT_NAME).cc',
            '<(mojo_output_dir)/mojo/ml_service/<(RULE_INPUT_NAME).h',
          ],
          'message': 'Generating mojo C++ bindings for ML Service from <(RULE_INPUT_PATH)',
          'action': [
            'python', '<(mojo_binding_generator)', '--use_bundled_pylibs',
            'generate', '<(RULE_INPUT_PATH)',
            '-o', '<(mojo_output_dir)',
            '--bytecode_path', '<(mojo_template_dir)',
            '-g', 'c++',
          ],
          'process_outputs_as_sources': 1,
        },
      ],
    },
  ],
}
