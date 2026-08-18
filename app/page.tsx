import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Textarea } from '@/components/ui/textarea'
import { Card, CardImage, CardContent, CardDescription, CardFooter, CardHeader, CardLabel, CardTitle } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'
import { Separator } from '@/components/ui/separator'
import { Label } from '@/components/ui/label'
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs'
import { Avatar, AvatarFallback } from '@/components/ui/avatar'
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select'

function Section({ title, children, dark = false }: { title: string; children: React.ReactNode; dark?: boolean }) {
  return (
    <section className={`py-14 border-b border-border last:border-none ${dark ? 'bg-foreground text-background -mx-8 px-8' : ''}`}>
      <p className={`text-[10px] tracking-widest uppercase mb-10 ${dark ? 'text-background/40' : 'text-muted-foreground'}`}>{title}</p>
      {children}
    </section>
  )
}

export default function Home() {
  return (
    <div className="min-h-screen bg-background">

      {/* Header */}
      <header className="border-b border-border px-8 py-5 flex items-center justify-between">
        <div className="flex items-center gap-6">
          <span className="text-xs text-muted-foreground">sunday/sunday™</span>
          <span className="text-xs text-muted-foreground">Design System</span>
        </div>
        <span className="text-xs text-muted-foreground">v1.0</span>
      </header>

      <main className="px-8">

        {/* ─── Typography ─── */}
        <Section title="Typography">
          <div className="space-y-6">
            <div>
              <p className="text-[10px] tracking-widest uppercase text-muted-foreground mb-4">Scale</p>
              <div className="space-y-3">
                <p className="text-5xl font-medium leading-none tracking-tight">Display Medium</p>
                <p className="text-3xl font-medium leading-tight">Heading Medium</p>
                <p className="text-xl font-medium">Title Medium</p>
                <p className="text-base font-light">Body Book — the quick brown fox jumps over the lazy dog</p>
                <p className="text-sm text-muted-foreground font-light">Secondary — supporting text and descriptions</p>
                <p className="text-xs text-muted-foreground">Caption — metadata and small details</p>
                <p className="text-[10px] tracking-widest uppercase">Label — uppercase tracking-widest</p>
              </div>
            </div>

            <Separator />

            {/* Slash section label — from proposal */}
            <div>
              <p className="text-[10px] tracking-widest uppercase text-muted-foreground mb-4">Section label (slash prefix)</p>
              <div className="flex items-baseline gap-6">
                <span className="text-muted-foreground text-sm">/</span>
                <span className="text-sm">Our Purpose</span>
              </div>
              <div className="flex items-baseline gap-6 mt-2">
                <span className="text-muted-foreground text-sm">/</span>
                <span className="text-sm">Industry</span>
              </div>
            </div>

            <Separator />

            {/* Quote block — from proposal */}
            <div>
              <p className="text-[10px] tracking-widest uppercase text-muted-foreground mb-6">Quote block</p>
              <div className="bg-secondary px-10 py-14 -mx-2">
                <blockquote className="text-3xl font-medium leading-tight max-w-3xl">
                  "A brand is no longer what we tell the consumer it is — it is what consumers tell each other it is."
                </blockquote>
                <div className="flex items-baseline gap-6 mt-8">
                  <span className="text-muted-foreground text-sm">/</span>
                  <span className="text-sm">Scott Cook</span>
                </div>
              </div>
            </div>
          </div>
        </Section>

        {/* ─── Colors ─── */}
        <Section title="Colors">
          <div className="flex flex-wrap gap-5">
            {[
              { name: 'Black', cls: 'bg-foreground', hex: '#000000' },
              { name: 'White', cls: 'bg-background border border-border', hex: '#FFFFFF' },
              { name: 'Muted', cls: 'bg-muted-foreground', hex: '#404040' },
              { name: 'Surface', cls: 'bg-secondary', hex: '#F4F4F4' },
              { name: 'Border', cls: 'bg-border', hex: '#E8E8E8' },
            ].map(color => (
              <div key={color.name} className="w-28">
                <div className={`${color.cls} h-16 mb-2`} />
                <p className="text-xs font-medium">{color.name}</p>
                <p className="text-[10px] text-muted-foreground font-mono">{color.hex}</p>
              </div>
            ))}
          </div>
        </Section>

        {/* ─── Buttons ─── */}
        <Section title="Buttons">
          <div className="space-y-10">
            <div>
              <p className="text-[10px] tracking-widest uppercase text-muted-foreground mb-5">Primary — underline + arrow</p>
              <div className="flex flex-wrap items-end gap-10">
                <Button>Vamos conversar ↗</Button>
                <Button size="sm">View case ↗</Button>
                <Button size="lg">Start a project ↗</Button>
                <Button disabled>Disabled ↗</Button>
              </div>
            </div>
            <div className="bg-foreground -mx-8 px-8 py-10">
              <p className="text-[10px] tracking-widest uppercase text-background/40 mb-5">Primary on dark</p>
              <button className="border-b border-background text-background font-light pb-0.5 text-sm hover:opacity-50 transition-all inline-flex items-center gap-1.5">
                Vamos conversar ↗
              </button>
            </div>
            <div>
              <p className="text-[10px] tracking-widest uppercase text-muted-foreground mb-5">Secondary actions</p>
              <div className="flex flex-wrap items-center gap-4">
                <Button variant="solid">Get started</Button>
                <Button variant="outline">Learn more</Button>
                <Button variant="ghost">Cancel</Button>
                <Button variant="destructive">Delete ↗</Button>
              </div>
            </div>
          </div>
        </Section>

        {/* ─── Badges ─── */}
        <Section title="Badges">
          <div className="space-y-6">
            <div className="flex flex-wrap gap-3">
              <Badge>Family and Frens Condition</Badge>
              <Badge>Brand Strategy</Badge>
              <Badge>UX & UI Design</Badge>
            </div>
            <div className="flex flex-wrap gap-3">
              <Badge variant="outline">Outline</Badge>
              <Badge variant="secondary">Secondary</Badge>
              <Badge variant="destructive">Destructive</Badge>
            </div>
          </div>
        </Section>

        {/* ─── Numbered List — from proposal p.5 ─── */}
        <Section title="Numbered List">
          <div className="max-w-3xl">
            {[
              { n: '01', title: 'Brand Strategy', desc: 'Clear direction for brands that want to grow through consistency, not luck. We translate ambition into strategy.' },
              { n: '02', title: 'Naming', desc: 'We create names with meaning, strong phonetics, and strategic intent. Built to last, sound right, and win people over.' },
              { n: '03', title: 'Verbal Identity', desc: 'Tone, language, and messaging that connect and sell. From tagline to bio, from pitch to manifesto.' },
              { n: '04', title: 'Visual Identity', desc: 'Design with precision. Visual systems that sustain presence and scalability.' },
              { n: '05', title: 'UX/UI Design', desc: 'Digital experiences with form, function, and flow. Where the brand meets the interface.' },
            ].map((item, i) => (
              <div key={item.n} className={`grid grid-cols-[3rem_1fr_2fr] gap-4 py-5 ${i < 4 ? 'border-b border-border' : ''}`}>
                <span className="text-xs text-muted-foreground pt-0.5">{item.n}</span>
                <span className="text-sm font-medium">{item.title}</span>
                <span className="text-sm text-muted-foreground leading-relaxed">{item.desc}</span>
              </div>
            ))}
          </div>
        </Section>

        {/* ─── Pricing — from proposal p.12 ─── */}
        <Section title="Pricing Display">
          <div className="bg-secondary p-10 max-w-2xl">
            <div className="grid grid-cols-2 gap-8 mb-6">
              <div>
                <p className="text-[10px] tracking-widest uppercase text-muted-foreground mb-1">Project</p>
                <p className="text-xl font-medium">Launch Website GOAT Decoded</p>
              </div>
              <div>
                <p className="text-[10px] tracking-widest uppercase text-muted-foreground mb-1">Deliverables</p>
                <p className="text-xl font-medium">10 weeks</p>
              </div>
            </div>
            <Separator />
            <div className="mt-6 space-y-1 text-sm text-muted-foreground">
              <p>1. Strategy and UX Design</p>
              <p>2. UI Design</p>
              <p>3. Development and Delivery</p>
            </div>
            <div className="mt-8">
              <p className="text-sm text-muted-foreground line-through">US$ 5.800</p>
              <div className="flex items-center gap-3 mt-1">
                <p className="text-3xl font-medium">US$ 4.000</p>
                <Badge>Family and Frens Condition</Badge>
              </div>
              <p className="text-xs text-muted-foreground mt-2">Payment in 4 parts — March, April, May, June</p>
            </div>
          </div>
        </Section>

        {/* ─── Form Elements ─── */}
        <Section title="Form Elements">
          <div className="max-w-2xl space-y-0">
            <div className="grid sm:grid-cols-2 gap-x-6">
              <Input placeholder="Qual o seu nome?" />
              <Input placeholder="Qual o seu email?" />
              <Input placeholder="Qual o nome da sua empresa?" />
              <Input placeholder="Qual o seu número?" />
            </div>
            <div className="mt-2">
              <Textarea placeholder="Conte-nos um pouco do seu projeto" rows={2} />
            </div>
            <div className="pt-8 space-y-6">
              <div>
                <p className="text-sm mb-4">Qual serviço você precisa para atingir seu objetivo?</p>
                <div className="flex flex-wrap gap-2">
                  {['Brand Strategy', 'Naming', 'Verbal ID', 'Visual ID', 'Packaging Design', 'UX/UI Design'].map((item, i) => (
                    <button key={item}
                      className={`px-4 py-2 text-sm border transition-colors ${i === 0 ? 'bg-foreground text-background border-foreground' : 'bg-transparent text-foreground border-border hover:border-foreground'}`}>
                      {item}
                    </button>
                  ))}
                </div>
              </div>
              <div>
                <p className="text-sm mb-4">Qual o valor que você espera investir?</p>
                <div className="flex flex-wrap gap-2">
                  {['Menor que 15mil', '15-20mil', '20-30mil', '30-50mil', '50-70mil', 'Acima de 100mil'].map(item => (
                    <button key={item}
                      className="px-4 py-2 text-sm border border-border bg-transparent text-foreground hover:border-foreground transition-colors">
                      {item}
                    </button>
                  ))}
                </div>
              </div>
            </div>
            <div className="pt-8 mt-8 border-t border-border space-y-1">
              <p className="text-[10px] tracking-widest uppercase text-muted-foreground mb-4">With label</p>
              <Label htmlFor="labeled">Company name</Label>
              <Input id="labeled" placeholder="Sunday to Sunday" />
            </div>
          </div>
        </Section>

        {/* ─── Cards ─── */}
        <Section title="Cards">
          <div className="grid sm:grid-cols-3 gap-8">
            <Card>
              <CardImage className="aspect-[4/3]">
                <img src="https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=600&q=80"
                  alt="" className="w-full h-full object-cover grayscale" />
              </CardImage>
              <CardHeader>
                <CardLabel>Brand Identity</CardLabel>
                <CardTitle>Decoded Studio</CardTitle>
              </CardHeader>
              <CardFooter>
                <a href="#" className="text-xs tracking-widest uppercase underline underline-offset-4 hover:text-muted-foreground transition-colors">View case ↗</a>
              </CardFooter>
            </Card>
            <Card className="border-t border-foreground pt-5">
              <CardHeader className="pt-0">
                <CardLabel>Service</CardLabel>
                <CardTitle>Visual Identity</CardTitle>
              </CardHeader>
              <CardContent>
                <CardDescription>A complete visual language that translates your brand strategy into a cohesive, distinctive identity.</CardDescription>
              </CardContent>
              <CardFooter>
                <a href="#" className="text-xs tracking-widest uppercase underline underline-offset-4 hover:text-muted-foreground transition-colors">Learn more ↗</a>
              </CardFooter>
            </Card>
            <Card className="bg-foreground text-background p-6">
              <CardHeader className="pt-0">
                <CardLabel className="text-background/50">Featured</CardLabel>
                <CardTitle className="text-background text-xl mt-2">Brands built to outlast trends.</CardTitle>
              </CardHeader>
              <CardContent>
                <CardDescription className="text-background/60 mt-3">Strategy-led design for founders who think long-term.</CardDescription>
              </CardContent>
              <CardFooter className="pt-6">
                <a href="#" className="text-xs tracking-widest uppercase text-background underline underline-offset-4 hover:opacity-60 transition-colors">Start a project ↗</a>
              </CardFooter>
            </Card>
          </div>
        </Section>

        {/* ─── Tabs ─── */}
        <Section title="Tabs">
          <Tabs defaultValue="overview" className="max-w-lg">
            <TabsList>
              <TabsTrigger value="overview">Overview</TabsTrigger>
              <TabsTrigger value="process">Process</TabsTrigger>
              <TabsTrigger value="deliverables">Deliverables</TabsTrigger>
            </TabsList>
            <TabsContent value="overview" className="mt-4">
              <p className="text-sm text-muted-foreground leading-relaxed">A complete brand identity system starting with strategy and ending with a full visual toolkit.</p>
            </TabsContent>
            <TabsContent value="process" className="mt-4">
              <p className="text-sm text-muted-foreground leading-relaxed">Discovery → Concept → Refinement → Delivery. Four phases over 6 weeks.</p>
            </TabsContent>
            <TabsContent value="deliverables" className="mt-4">
              <p className="text-sm text-muted-foreground leading-relaxed">Logo suite, colour palette, typography, brand guidelines PDF, and asset library.</p>
            </TabsContent>
          </Tabs>
        </Section>

        {/* ─── Utilities ─── */}
        <Section title="Utilities">
          <div className="space-y-8">
            <div>
              <p className="text-[10px] tracking-widest uppercase text-muted-foreground mb-3">Avatars</p>
              <div className="flex gap-3">
                <Avatar><AvatarFallback>LR</AvatarFallback></Avatar>
                <Avatar><AvatarFallback>RG</AvatarFallback></Avatar>
                <Avatar><AvatarFallback>S:S</AvatarFallback></Avatar>
              </div>
            </div>
            <div>
              <p className="text-[10px] tracking-widest uppercase text-muted-foreground mb-3">Separators</p>
              <div className="space-y-4 max-w-sm">
                <Separator />
                <div className="flex items-center gap-4">
                  <Separator className="flex-1" />
                  <span className="text-[10px] tracking-widest uppercase text-muted-foreground">or</span>
                  <Separator className="flex-1" />
                </div>
              </div>
            </div>
          </div>
        </Section>

      </main>

      <footer className="border-t border-border px-8 py-6 flex items-center justify-between">
        <p className="text-[10px] tracking-widest uppercase text-muted-foreground">sunday/sunday design system</p>
        <p className="text-[10px] text-muted-foreground">©2026</p>
      </footer>

    </div>
  )
}
