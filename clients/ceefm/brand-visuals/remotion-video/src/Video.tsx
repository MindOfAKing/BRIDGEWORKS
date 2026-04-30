import React from 'react';
import {
  AbsoluteFill,
  Easing,
  Img,
  interpolate,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from 'remotion';

export type Lang = 'EN' | 'HU';
export type Variant = '16x9' | '1x1' | '9x16';

type Props = {
  duration: 15 | 30;
  lang: Lang;
  variant: Variant;
};

const BRAND = {
  green: '#1C3D2A',
  greenLight: '#2D5942',
  gold: '#B8860B',
  ivory: '#F5F0E8',
  white: '#FFFFFF',
  muted: '#E2DDD3',
};

const copy = {
  EN: {
    hook: '9.4 cleanliness score.',
    proof: 'Sustained 24 months at Limehome Budapest.',
    category15: 'Premium facility management.',
    category30: 'Premium facility management for Hungary.',
    sectors15: ['Hotels.', 'Aparthotels.', 'Residential.'],
    sectors30: ['Hotels and aparthotels.', 'Residential portfolios.', 'Student housing.'],
    differentiator15: 'Contract-based. KPI-led. Operating since 2010.',
    differentiators30: ['Contract-based.', 'Dedicated account manager.', 'Monthly KPI reporting.'],
    audit: 'EU-compliant audit trails. Same teams every visit.',
    trust: [
      ['50+', 'properties managed'],
      ['98%', 'client retention'],
      ['15 years', 'operating since 2010'],
    ],
    audience: 'Property managers, hotel GMs, condo boards.',
    cta: 'Request a free site assessment →',
    url: 'ceefm.eu/contact',
  },
  HU: {
    hook: '9.4-es tisztasági pontszám.',
    proof: '24 hónapja a Limehome Budapesten.',
    category15: 'Prémium létesítménygazdálkodás.',
    category30: 'Prémium létesítménygazdálkodás Magyarországon.',
    sectors15: ['Szállodák.', 'Apartmanhotelek.', 'Lakóparkok.'],
    sectors30: ['Szállodák és apartmanhotelek.', 'Lakossági portfóliók.', 'Diákszállások.'],
    differentiator15: 'Szerződés alapú. KPI-vezérelt. 2010 óta.',
    differentiators30: ['Szerződés alapú.', 'Dedikált ügyfélmenedzser.', 'Havi KPI-jelentés.'],
    audit: 'EU-megfelelő audit nyomvonal. Ugyanaz a csapat minden látogatáskor.',
    trust: [
      ['50+', 'kezelt ingatlan'],
      ['98%', 'ügyfélmegtartás'],
      ['15 év', '2010 óta működünk'],
    ],
    audience: 'Társasházak, szállodák, ingatlankezelők.',
    cta: 'Kérjen ingyenes helyszíni felmérést →',
    url: 'ceefm.eu/hu/kapcsolat',
  },
};

const inOut = (frame: number, start: number, end: number) => {
  const inOpacity = interpolate(frame, [start, start + 10], [0, 1], {
    easing: Easing.out(Easing.cubic),
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  const outOpacity = interpolate(frame, [end - 10, end], [1, 0], {
    easing: Easing.in(Easing.cubic),
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  return Math.min(inOpacity, outOpacity);
};

const sceneActive = (frame: number, start: number, end: number) => inOut(frame, start, end);

const GoldRule: React.FC<{start: number; y?: number; width?: number}> = ({start, y = 0, width = 330}) => {
  const frame = useCurrentFrame();
  const progress = interpolate(frame, [start, start + 8], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
    easing: Easing.out(Easing.cubic),
  });

  return (
    <div
      style={{
        width: width * progress,
        height: 5,
        background: BRAND.gold,
        marginTop: y,
      }}
    />
  );
};

const Scene: React.FC<{
  start: number;
  end: number;
  children: React.ReactNode;
  align?: 'center' | 'left';
}> = ({start, end, children, align = 'center'}) => {
  const frame = useCurrentFrame();
  const opacity = sceneActive(frame, start, end);
  const y = interpolate(opacity, [0, 1], [22, 0]);

  return (
    <div
      style={{
        position: 'absolute',
        inset: 0,
        opacity,
        transform: `translateY(${y}px)`,
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'center',
        alignItems: align === 'center' ? 'center' : 'flex-start',
      }}
    >
      {children}
    </div>
  );
};

const BigText: React.FC<{children: React.ReactNode; variant: Variant; compact?: boolean}> = ({
  children,
  variant,
  compact,
}) => (
  <div
    style={{
      fontFamily: 'Georgia, Cormorant Garamond, serif',
      fontSize: variant === '9x16' ? (compact ? 76 : 92) : variant === '1x1' ? 82 : 96,
      lineHeight: 1.04,
      color: BRAND.white,
      fontWeight: 700,
      textAlign: 'center',
      maxWidth: variant === '9x16' ? 870 : variant === '1x1' ? 900 : 1220,
    }}
  >
    {children}
  </div>
);

const SmallText: React.FC<{children: React.ReactNode; variant: Variant}> = ({children, variant}) => (
  <div
    style={{
      fontFamily: 'Inter, Arial, sans-serif',
      fontSize: variant === '9x16' ? 36 : variant === '1x1' ? 31 : 34,
      lineHeight: 1.34,
      color: BRAND.muted,
      marginTop: 28,
      textAlign: 'center',
      maxWidth: variant === '9x16' ? 850 : variant === '1x1' ? 780 : 1120,
      fontWeight: 600,
    }}
  >
    {children}
  </div>
);

const StackLines: React.FC<{lines: string[]; variant: Variant; start: number}> = ({lines, variant, start}) => {
  const frame = useCurrentFrame();
  return (
    <div style={{display: 'flex', flexDirection: 'column', gap: variant === '9x16' ? 24 : 18}}>
      {lines.map((line, index) => {
        const opacity = interpolate(frame, [start + index * 5, start + index * 5 + 10], [0, 1], {
          extrapolateLeft: 'clamp',
          extrapolateRight: 'clamp',
        });
        return (
          <div
            key={line}
            style={{
              opacity,
              fontFamily: 'Inter, Arial, sans-serif',
              fontSize: variant === '9x16' ? 52 : variant === '1x1' ? 48 : 54,
              color: BRAND.ivory,
              fontWeight: 800,
              textAlign: 'center',
            }}
          >
            {line}
          </div>
        );
      })}
    </div>
  );
};

const TrustBlock: React.FC<{items: string[][]; variant: Variant; start: number}> = ({items, variant, start}) => {
  const frame = useCurrentFrame();
  const vertical = variant === '9x16';
  return (
    <div
      style={{
        display: 'flex',
        flexDirection: vertical ? 'column' : 'row',
        gap: vertical ? 28 : 34,
        alignItems: 'center',
        justifyContent: 'center',
      }}
    >
      {items.map(([value, label], index) => {
        const opacity = interpolate(frame, [start + index * 8, start + index * 8 + 12], [0, 1], {
          extrapolateLeft: 'clamp',
          extrapolateRight: 'clamp',
        });
        return (
          <div key={value} style={{opacity, minWidth: vertical ? 520 : 260, textAlign: 'center'}}>
            <div
              style={{
                fontFamily: 'Georgia, Cormorant Garamond, serif',
                fontSize: vertical ? 76 : variant === '1x1' ? 68 : 74,
                color: BRAND.gold,
                lineHeight: 1,
                fontWeight: 700,
              }}
            >
              {value}
            </div>
            <div
              style={{
                fontFamily: 'Inter, Arial, sans-serif',
                fontSize: vertical ? 28 : 24,
                color: BRAND.muted,
                marginTop: 12,
                fontWeight: 700,
              }}
            >
              {label}
            </div>
          </div>
        );
      })}
    </div>
  );
};

export const CEEFMVideo: React.FC<Props> = ({duration, lang, variant}) => {
  const frame = useCurrentFrame();
  const {width, height} = useVideoConfig();
  const text = copy[lang];
  const vertical = variant === '9x16';
  const square = variant === '1x1';
  const pad = vertical ? 70 : square ? 56 : 84;
  const logoSize = vertical ? 82 : 74;
  const textureX = interpolate(frame, [0, duration * 30], [0, 8]);
  const ruleProgress = interpolate(frame, [0, 12], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
    easing: Easing.out(Easing.cubic),
  });

  const commonScenes =
    duration === 15
      ? {
          hook: [0, 105],
          category: [105, 180],
          sectors: [180, 270],
          diff: [270, 360],
          cta: [360, 450],
        }
      : {
          hook: [0, 135],
          category: [135, 210],
          sectors: [210, 330],
          diff: [330, 540],
          trust: [540, 660],
          audience: [660, 780],
          cta: [780, 900],
        };
  const trustScene = duration === 30 ? [540, 660] : null;
  const audienceScene = duration === 30 ? [660, 780] : null;

  return (
    <AbsoluteFill
      style={{
        background: `linear-gradient(135deg, ${BRAND.green}, ${BRAND.greenLight})`,
        overflow: 'hidden',
      }}
    >
      <div
        style={{
          position: 'absolute',
          inset: 0,
          backgroundImage:
            'repeating-linear-gradient(135deg, rgba(245,240,232,0.18) 0px, rgba(245,240,232,0.18) 1px, transparent 1px, transparent 22px)',
          transform: `translateX(${textureX}px)`,
          opacity: 0.45,
        }}
      />
      <div
        style={{
          position: 'absolute',
          width: vertical ? 520 : 700,
          height: vertical ? 520 : 700,
          borderRadius: '50%',
          border: `72px solid rgba(184,134,11,0.18)`,
          right: vertical ? -260 : -220,
          bottom: vertical ? 70 : -250,
        }}
      />

      <div
        style={{
          position: 'absolute',
          top: pad,
          right: pad,
          display: 'flex',
          alignItems: 'center',
          gap: 16,
          opacity: interpolate(frame, [0, 14], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'}),
        }}
      >
        <div
          style={{
            fontFamily: 'Inter, Arial, sans-serif',
            fontSize: vertical ? 24 : 22,
            color: BRAND.ivory,
            fontWeight: 800,
          }}
        >
          CEEFM Kft
        </div>
        <Img src={staticFile('ceefm-logo.png')} style={{width: logoSize, height: logoSize, objectFit: 'contain'}} />
      </div>

      <div
        style={{
          position: 'absolute',
          left: 0,
          bottom: vertical ? 52 : 42,
          height: 5,
          width: width * ruleProgress,
          background: BRAND.gold,
        }}
      />

      <div style={{position: 'absolute', inset: pad}}>
        <Scene start={commonScenes.hook[0]} end={commonScenes.hook[1]}>
          <BigText variant={variant}>{text.hook}</BigText>
          <GoldRule start={10} y={26} width={vertical ? 300 : 360} />
          <SmallText variant={variant}>{text.proof}</SmallText>
        </Scene>

        <Scene start={commonScenes.category[0]} end={commonScenes.category[1]}>
          <BigText variant={variant} compact={lang === 'HU'}>
            {duration === 15 ? text.category15 : text.category30}
          </BigText>
        </Scene>

        <Scene start={commonScenes.sectors[0]} end={commonScenes.sectors[1]}>
          <StackLines
            lines={duration === 15 ? text.sectors15 : text.sectors30}
            variant={variant}
            start={commonScenes.sectors[0] + 8}
          />
        </Scene>

        <Scene start={commonScenes.diff[0]} end={commonScenes.diff[1]}>
          {duration === 15 ? (
            <>
              <SmallText variant={variant}>{text.differentiator15}</SmallText>
              <GoldRule start={commonScenes.diff[0] + 8} y={24} width={vertical ? 360 : 470} />
            </>
          ) : (
            <>
              <StackLines lines={text.differentiators30} variant={variant} start={commonScenes.diff[0] + 5} />
              <SmallText variant={variant}>{text.audit}</SmallText>
              <GoldRule start={commonScenes.diff[0] + 40} y={24} width={vertical ? 420 : 530} />
            </>
          )}
        </Scene>

        {duration === 30 && trustScene && audienceScene ? (
          <>
            <Scene start={trustScene[0]} end={trustScene[1]}>
              <TrustBlock items={text.trust} variant={variant} start={trustScene[0] + 8} />
            </Scene>
            <Scene start={audienceScene[0]} end={audienceScene[1]}>
              <SmallText variant={variant}>{text.audience}</SmallText>
            </Scene>
          </>
        ) : null}

        <Scene start={commonScenes.cta[0]} end={duration * 30 + 1}>
          <div
            style={{
              border: `2px solid ${BRAND.gold}`,
              borderRadius: 8,
              padding: vertical ? '34px 38px' : '30px 42px',
              background: 'rgba(15, 26, 46, 0.22)',
              textAlign: 'center',
              maxWidth: vertical ? 850 : 1060,
            }}
          >
            <div
              style={{
                fontFamily: 'Inter, Arial, sans-serif',
                fontSize: vertical ? 48 : square ? 42 : 46,
                color: BRAND.white,
                fontWeight: 900,
                lineHeight: 1.15,
              }}
            >
              {text.cta}
            </div>
            <div
              style={{
                fontFamily: 'Inter, Arial, sans-serif',
                fontSize: vertical ? 30 : 28,
                color: BRAND.muted,
                marginTop: 18,
                fontWeight: 700,
              }}
            >
              {text.url}
            </div>
          </div>
        </Scene>
      </div>

      <div
        style={{
          position: 'absolute',
          left: pad,
          bottom: vertical ? 82 : 70,
          fontFamily: 'Inter, Arial, sans-serif',
          fontSize: vertical ? 22 : 20,
          color: 'rgba(245,240,232,0.72)',
          fontWeight: 700,
        }}
      >
        Budapest · Hungary
      </div>
    </AbsoluteFill>
  );
};
