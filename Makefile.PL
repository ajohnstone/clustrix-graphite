use ExtUtils::MakeMaker;

WriteMakefile(
    NAME      => 'clustrix-graphite',
    VERSION   => '0.1',
    EXE_FILES => [ <bin/*> ],
    MAN1PODS  => {
      'docs/clustrix-graphite.pod' => 'blib/man1/clustrix-graphite.1p',
      map {
         (my $name = $_) =~ s/^bin.//;
         $_ => "blib/man1/$name.1p";
      } <bin/*>
    },
    MAN3PODS     => {}, # man(3) pages are for C libs
    PREREQ_PM    => {
        DBI           => 1.46,
        DBD::mysql    => 3.0000_0,
    },
);
