import Vue from "vue";
import Annotations from "../../../src/components/Annotations";
import { shallow } from "vue-test-utils";


describe("HelloWorld.vue", () => {
  it("should render correct contents", () => {
    const vm = shallow(Annotations, {
      mocks: {
        $route: {
          query: { bookId: 123 }
        }
      }
    }).vm;

    expect(vm.$el.textContent).toMatchInlineSnapshot();
  });
});
